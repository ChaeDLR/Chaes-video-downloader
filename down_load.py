from selenium import webdriver
from pytube import YouTube, Playlist
import os

class Down_Load:
	
	def __init__(self, window):
		"""download"""
		self.destinationPath = 'Videos/'
		self.window = window

	def videotube(self, url):
		"""download video"""

		self.ytVideo = YouTube(url)

		# list the streams
		self.streamList = self.streams_list()
	
	def select_stream(self):
		"""fetch the users selected stream to download"""
		#self.user_selected_stream = self.window.
		#self.usrStream = self.ytVideo.streams[]
		#self.usrStream.download(self.destinationPath)
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