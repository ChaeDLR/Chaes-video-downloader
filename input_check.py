import re

class Input_Check:
	"""inputclass"""
	def __init__(self):
		"""init for this test"""
		self.url_match = False
		self.youtube_check = re.compile(r'youtube.com')

	def url_text_check(self, textstring):
		"""used to check a string"""
		isYoutubeUrl = self.youtube_check.search(textstring)
		if isYoutubeUrl:
			print("URl passed check")
			return True