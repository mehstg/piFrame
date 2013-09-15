#!/usr/bin/python

"""piFrame.py: This script is designed to search Twitter for a specific hashtag and display tweets containing an image via the FEH image viewer"""
"""Requires the Tweepy libraries. Visit https://github.com/tweepy/tweepy for more information"""

__author__      = "Paul Braham"
__copyright__   = "Copyright 2013, Released under the GPLv3 License - more information at http://www.gnu.org/licenses/"

#imports
import sys
import tweepy
import argparse
import subprocess

#Twitter OAuth keys - For more info visit https://dev.twitter.com/docs/auth/oauth/faq
consumer_key=""
consumer_secret=""
access_key = ""
access_secret = ""

#Specific hashtag you wish to search for
hashtag = '#piframe'

# Argument parser - Allows piframe to accept command line arguments in the form of:
parser = argparse.ArgumentParser()
parser.add_argument('-i','--images', help="Returns image URL's for tweets", action='store_true')
parser.add_argument('-t','--text', help='Returns tweet body text', action='store_true')
#parser.add_argument('-o','--outputall', help='Returns image and text formatted for FEH', action='store_true')
args = parser.parse_args()



def main():
	
	#Connect to Twitter v1.1 API using OAuth
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)

	if args.images:
		print retrieveTweetImages(api,hashtag)

	elif args.text:
		print retrieveTweetBody(api,hashtag)
	
#	elif args.outputall:
#		print retrieveAll(api,hashtag)


# Function to retrieve Tweet Images based on given hashtag. Expects two arguments, a currently open Twitter session and a hashtag string.
def retrieveTweetImages(apiSession,searchtag):
	
	imageURL = ''
	for tweet in tweepy.Cursor(apiSession.search,q=searchtag,count=5,include_entities=True).items(5):
		#print tweet.text
		try:
			for image in  tweet.entities['media']:
				imageURL +=  str(image['media_url']) + ' '
		except KeyError:
			pass


	#return list of retrieved media URL's.
	return imageURL



# Function to retrieve Tweet text based on given hashtag.
def retrieveTweetBody(apiSession,searchtag):
	tweets = ''
	for tweet in tweepy.Cursor(apiSession.search,q=searchtag,count=5,include_entities=True).items(5):
		tweets += str(tweet.created_at) + '|' + str(tweet.text) + ','

	return tweets


# Code below commented out, will possibly be used in future.
#def retrieveAll(apiSession,searchtag):
#	output = ''
#	for tweet in tweepy.Cursor(apiSession.search,q=searchtag,count=1,include_entities=True).items(1):
#       	#print tweet.text
#                try:
#                        for image in  tweet.entities['media']:
#                                output  += " --info '" + str(tweet.text) + " " + str(image['media_url']) + "' ,"
#                except KeyError:
#                        pass

	#return list of retrieved media URL's. Strip last comma from string.
#        return output[:-1]


# Run Slideshow - Invokes FEH with the correct command line aruments
#def runSlideshow(delay,images):
#	feh = subprocess.Popen(['/usr/bin/feh', '--quiet --full-screen --slideshow-delay', delay, images] shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

#Invoke main function
if __name__ == "__main__":
    main()
