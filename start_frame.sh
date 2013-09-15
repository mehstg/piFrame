#!/bin/sh
#
#

# Change number below to the duration, in seconds
# for each photo to be displayed
DELAY="10"



# hide the cursor after 2 seconds
#/usr/bin/unclutter -idle 2 &

#Retrieve twitter images for hashtag using piFrame python script
TWITPICS=$(/home/pi/piFrame/piFrame.py -i)

#echo $TWITPICS


# Start slide show
/usr/bin/feh --quiet --full-screen --slideshow-delay $DELAY $TWITPICS &

exit 0
