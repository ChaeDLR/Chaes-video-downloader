from selenium import webdriver
from pytube import YouTube, Playlist
from textchecks import SearchingPro
import os
import re

class Down_Load:
	
    def __init__(self):
        """download"""
        self.urlCheck = SearchingPro()

    def videotube(self):
    	"""download video"""

    	print("Chae's Downloader")
    	#print("Enter url: ")
    	url = input('Enter URL: ')

    	while self.urlCheck.isUrl(url) == False:
    		print("Try again...")
    		url = input('Enter URL: ')

    	print("Fetching video...")
    	ytVideo = YouTube(url)

    	
    	for i in range(0, len(ytVideo.streams)):
    		print("Number: {} | {}".format(i, ytVideo.streams[i]))
    	print("Choose a stream number:")
    	streamChoice = input()

    	destinationPath = 'Videos/'

    	print("Downloading...")
    	usrStream = ytVideo.streams[int(streamChoice)]
    	usrStream.download(destinationPath)
    	print("Done!")


if __name__ == "__main__":

	download = Down_Load()
	download.videotube()