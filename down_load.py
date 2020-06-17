from selenium import webdriver
from pytube import YouTube, Playlist
import os
import re

class Down_Load:
	
	def __init__(self):
		"""download"""
		self.destinationPath = 'Videos/'

	def videotube(self):
		"""download video"""

		print("Chae's Downloader")
		#print("Enter url: ")
		#url = self.input_check.url_prompt()

		print("Fetching video...")
		self.ytVideo = YouTube(url)

		# list the streams
		streamList = self.streams_list()
		for i in enumerate(streamList):
			print(streamList[i])

		print("Downloading...")
		usrStream = self.ytVideo.streams[int(streamChoice)]
		usrStream.download(self.destinationPath)
		print("Done!")
	
	def streams_list(self):
		"""return a list of streams available """
		sl = []

		for _, stream in enumerate(self.ytVideo.streams):
			sl.append(stream)
			#print("Number: {} | {}".format(i, self.ytVideo.streams[i]))

		#print("Choose a stream number:")
		#streamChoice = input()
		return sl


if __name__ == "__main__":

	download = Down_Load()
	download.videotube()