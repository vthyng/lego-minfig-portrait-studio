# lego-minfig-portrait-studio
These files are related to Vince's Lego Minfig Portrait Studio project.  This code expects that it is running on a Raspberry Pi with a camera module and rclone is configured to a cloud provider.  It has been tested on a Raspberry Pi `3` and `Zero W`.

# Prerequisites
Install and configure rclone to a cloud provider: https://github.com/rclone/rclone

# Installation
Clone this repo to /home/pi/lego-minfig-portrait-studio/
Add `python3 /home/pi/lego-minfig-portrait-studio/camera.py` to your `/etc/rc.local` file above the `exit 0` line.
