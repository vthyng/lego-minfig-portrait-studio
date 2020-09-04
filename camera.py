"""Camera software for Lego Minfig Portrait Studio."""

from datetime import datetime
from gpiozero import Button, LED
from time import sleep
from os import mkdir
import subprocess

button = Button(16)
button.hold_time = 6

light = LED(14)


# Flash light 3 times to indicate camera program is running
for x in range(3):
    light.off()
    sleep(.2)
    light.on()
    sleep(.2)

# on() turns OFF the LED because it pulls signal high on the pin
light.on()


def shutdown_pi():
    """Function to shutdown pi, called when button is pressed for over 6s."""
    # Flash light 3 times to indicate camera program is running
    light.on()
    for x in range(3):
        light.off()
        sleep(.2)
        light.on()
        sleep(.2)

    print('shutting down')
    command = '/usr/bin/sudo /sbin/shutdown now'
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    process.communicate()[0]


def capture_picture():
    """Function to take picture and sync to cloud."""
    # light on
    light.off()
    print('Taking picture')

    # get timestamp for filename
    time = str(datetime.now()).replace(':', '').replace(' ', '_')[:17]
    print('time is {}'.format(time))

    # make sure pics folder exists
    try:
        mkdir('pics')
    except FileExistsError:
        pass

    command = '/usr/bin/raspistill -t 500 -o pics/{}.jpg'.format(time)
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    process.communicate()[0]
    light.on()
    print('Finished taking picture')

    print('Copying to cloud')

    command = 'rclone copy pics/{}.jpg remote:'.format(time)
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    process.communicate()[0]
    print('Finished copying to cloud')

    # light on
    light.off()
    sleep(.2)

    # light off
    light.on()


button.when_held = shutdown_pi

while True:

    button.wait_for_press()
    button.wait_for_release()

    capture_picture()
