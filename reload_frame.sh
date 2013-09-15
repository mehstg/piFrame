#!/bin/sh
#
#  Bash script part of piFrame
#  piFrame.py: This script is designed to search Twitter for a specific hashtag and display tweets containing an image via the FEH image$
#  reload_frame.sh: Called via cron job to reload the FEH image viewer with new images periodically
#
#  author      = "Paul Braham"
#  copyright   = "Copyright 2013, Released under the GPLv3 License - more information at http://www.gnu.org/licenses/"
#
# Change number below to the duration, in seconds
# for each photo to be displayed
DELAY="10"

# Set display so that the script will effect
# the screen on the frame
export DISPLAY=:0

# Stop the currently running Slide show
killall feh

sleep 2s

#Retrieve twitter images for hashtag using piFrame python script
TWITPICS=$(/home/pi/piFrame/piFrame.py -i)

#echo $TWITPICS


# Start slide show
/usr/bin/feh --quiet --full-screen --slideshow-delay $DELAY $TWITPICS &


exit 0
