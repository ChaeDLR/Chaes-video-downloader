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
        # Create the filtered list as soon as the video is fetched
        self.user_video_available_resolutions = self.input_check.available_resolutions(
            self.streamList)

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

    def filter_streams(self, streamslist, useroption):
        """ filter the streams using the user selection"""
        sl = []
        for _, stream in enumerate(streamslist):
            sl.append(stream)
        sl = list(dict.fromkeys(sl))
        return sl
