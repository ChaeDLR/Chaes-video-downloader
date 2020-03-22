from selenium import webdriver
from pytube import YouTube, Playlist
from textchecks import SearchingPro
import os
import re

class down_load:

    def __init__(self):
        """download"""
        self.urlCheck = SearchingPro()

    def videotube(self):
    	"""download video"""

    	print("Chae's Downloader")
    	print("Enter url: ")
    	url = input()

    	while self.urlCheck.isUrl(url) == False:
    		print("Try again...")
    		url = input()

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

	Download = down_load()
	Download.videotube()
