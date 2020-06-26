import re

class Input_Check:
	"""inputclass"""

	def __init__(self):
		"""init for this test"""

		self.url_match = False
		self.youtube_check = re.compile(r'youtube.com/watch')
		self.audio_only_check = re.compile(r'acodec')
		self.video_only_check = re.compile(r'vcodec')
		self.both_video_audio_check = re.compile(r'False')
		self.webm_format_check = re.compile(r'webm')
		self.mp4_format_check = re.compile(r'mp4')

	def stream_format(self, streamlist, formatchoice):
		""" return stream format choice index """
		# finish returns here #############
		if formatchoice == "webm":
			for num, stream in enumerate(streamlist):
				self.webm_format_check.search(stream)
		elif formatchoice == "mp4":
			for num, stream in enumerate(streamlist)
				self.mp4_format_check.search(stream)
		
			

	def url_text_check(self, textstring):
		""" check that a string is a youtube.com/watch url """
		isYoutubeUrl = self.youtube_check.search(textstring)
		if isYoutubeUrl:
			print("URl passed check")
			return True

	def audio_only(self, streamlist):
		""" take stream list and output list of audio streams only """

		# loop through the streamlist 
		for num, stream in enumerate(streamlist):
			self.audio_only_stream = self.audio_only_check.search(stream)
			if self.audio_only_stream != None:
				return num

	def video_only(self, streamlist):
		""" take stream list and output list of video streams only """

		# loop through the streamlist
		for num, stream in enumerate(streamlist):
			self.video_only_stream = self.video_only_check.search(stream)
			if self.video_only_stream != None:
				return num

	def video_audio(self, streamlist):
		""" take stream list and remove the audio and video only streams """

		# loop through the streamlist
		for num, stream in enumerate(streamlist):
			self.both_stream = self.both_video_audio_check.search(stream)
			if self.both_stream != None:
				return num