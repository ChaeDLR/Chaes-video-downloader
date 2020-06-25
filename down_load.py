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
		print("using url")
		self.ytVideo = YouTube(url)
		print("grabbing stream list")
		# list the streams
		self.streamList = self.streams_list()
	
	def select_stream(self, selection):
		"""fetch the users selected stream to download"""

		self.user_selected_stream = selection
		self.usrStream = self.ytVideo.streams[selection]
		self.usrStream.download(self.destinationPath)
	
	def streams_list(self):
		"""return a list of streams available """
		sl = []
		for _, stream in enumerate(self.ytVideo.streams):
			sl.append(stream)
		return sl