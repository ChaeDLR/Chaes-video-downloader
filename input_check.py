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
		self.check_for_resolution = re.compile(r'res="(\d\d\d\d?)p"')

	def available_resolutions(self, streamlist):
		""" take the streamlist and output available resolutions in a list """
		stream_list = self.check_for_resolution.findall(str(streamlist))
		available_resolutions_list = []
		for stream in stream_list:
			available_resolutions_list.append(stream)
		return available_resolutions_list

	def stream_format(self, streamlist, formatchoice):
		""" return stream format choice index """
		if formatchoice == "webm":
			for num, stream in enumerate(streamlist):
				if self.webm_format_check.search(stream):
					return num
		elif formatchoice == "mp4":
			for num, stream in enumerate(streamlist):
				if self.mp4_format_check.search(stream):
					return num
		else:
			return False
			

	def url_text_check(self, textstring):
		""" check that a string is a youtube.com/watch url """
		isYoutubeUrl = self.youtube_check.search(textstring)
		if isYoutubeUrl:
			print("URl passed check")
			return True

	def audio_only(self, streamlist):
		""" take stream list and output list of audio streams only """
		audio_only_streams_list = []
		# loop through the streamlist 
		for _, stream in enumerate(streamlist):
			audio_only_stream = self.audio_only_check.search(str(stream))
			if audio_only_stream != None:
				audio_only_streams_list.append(stream)
		return audio_only_streams_list

	def video_only(self, streamlist):
		""" take stream list and output list of video streams only """
		video_only_streams_list = []
		# loop through the streamlist
		for _, stream in enumerate(streamlist):
			video_only_stream = self.video_only_check.search(stream)
			if video_only_stream != None:
				video_only_streams_list.append(stream)
		return video_only_streams_list

	def video_audio(self, streamlist):
		""" take stream list and remove the audio and video only streams """
		video_audio_streams_list = []
		# loop through the streamlist
		for _, stream in enumerate(streamlist):
			video_audio_stream = self.both_video_audio_check.search(stream)
			if video_audio_stream != None:
				video_audio_streams_list.append(stream)
		return video_audio_streams_list