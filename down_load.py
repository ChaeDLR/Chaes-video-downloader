from selenium import webdriver
from pytube import YouTube, Playlist
from input_check import Input_Check
import os
import re

class Down_Load:
	
	def __init__(self):
		"""download"""
		self.input_check = Input_Check()

	def videotube(self):
		"""download video"""

		print("Chae's Downloader")
		#print("Enter url: ")
		url = self.input_check.url_prompt()

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