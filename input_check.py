import pyinputplus as pyip
import re

class Input_Check:
	"""inputclass"""
	def __init__(self):
		"""init for this test"""
		self.url_match = False
		self.youtube_check = re.compile(r'youtube.com')

	def url_prompt(self):
		print("Enter a YouTube URL")
		self.user_url = pyip.inputURL()
		user_input_check = self.youtube_check.search(self.user_url)
		if user_input_check:
			self.user_url = str(self.user_url)
			return self.user_url

	def url_text_check(self, textstring):
		"""used to check a string"""
		isYoutubeUrl = self.youtube_check.search(textstring)
		if isYoutubeUrl:
			print(textstring)
			return True