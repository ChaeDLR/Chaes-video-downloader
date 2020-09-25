from selenium import webdriver
from pytube import YouTube, Playlist
import os


class Down_Load:
    def __init__(self):
        """ Initialize class 
        download a youtube video
        """
        self.destinationPath = 'Downloaded_Videos/'

    def videotube(self, url):
        """download video
        """
        # Create a youtube object with the users url
        self.ytVideo = YouTube(url)
        streams_list = self.ytVideo.streams
        return streams_list

    def select_stream(self, selectionindex):
        """fetch the users selected stream to download"""
        usrStream = self.ytVideo.streams[selectionindex]

        usrStream.download(self.destinationPath)
