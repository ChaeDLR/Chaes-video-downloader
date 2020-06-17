import tkinter as tk
from input_check import Input_Check
from down_load import Down_Load

root = tk.Tk()
root.title("Chae's video downloader ")
# root.iconbitmap()
root.geometry("400x400")
root.configure(background='#4f97a3')

class VideoDownloader:
	"""Video downloader class"""

	def __init__(self, master=None):
		"""init downloader variables"""
		self.frame = tk.Frame(master)
		self.frame.pack()

		self.input_check = Input_Check()
		self.down_load = Down_Load(self)

		self.master = master

		# tk.OptionsMenu(master, func, *list, command=#command)
		self._display_widets()

	def _display_widets(self):
		"""widget organizer"""
		self._url_entry_box()
		self._enter_button()

	def _enter_button(self):

		self.enter_button = tk.Button(self.master, text="Enter", command=self._button_function)
		#self.enter_button.bind("<Button-1>", self.button_function())
		self.enter_button.pack(pady=20)

	def _button_function(self):
		"""get and check user input"""
		self.initial_user_input = self.entry_box.get()
		if self.input_check.url_text_check(self.initial_user_input):
			# if the user input is indeed a youtube url we want to get the streams
			self.down_load.videotube(self.initial_user_input)
			# disable the entry field
			self.entry_box.destroy()
			# display listbox
			self._streams_listbox()

	def _select_stream(self):
		"""take the streams and separate them by type"""

		
	def _streams_listbox(self):
		"""take and display the stream options for a url"""
		# stream list 
		self.stream_list = self.down_load.streamList
		self.stream_list_box = tk.Listbox(self.master, width=30)
		self.stream_list_box.pack(pady=20)
		for i in enumerate(self.stream_list):
			# insert takes index and string 
			self.stream_list_box.insert(0, i)

	def _url_entry_box(self):
		"""entry bos for user url"""
		self.entry_box = tk.Entry(self.master, )
		self.entry_box.pack(pady=20)

	

if __name__ == '__main__':
	window = VideoDownloader(root)
	root.mainloop()
