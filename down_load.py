from selenium import webdriver
from pytube import YouTube, Playlist
import os

class Down_Load:
	
	def __init__(self, window, inputcheck):
		"""download"""
		self.destinationPath = 'Videos/'
		self.window = window
		self.input_check = inputcheck

	def videotube(self, url):
		"""download video"""
		print("using url")
		self.ytVideo = YouTube(url)
		print("grabbing stream list")
		# list the streams
		self.streamList = self.streams_list()
		for i in self.streamList:
			print(i)
	
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

	def filter_streams(self, useroption):
		""" filter the streams using the user selection"""
