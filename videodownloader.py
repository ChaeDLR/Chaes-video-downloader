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

		# window manager variables
		self.window_state = 0
		self.change_widgets = False
		# tk.OptionsMenu(master, func, *list, command=#command)
		self._display_widets(self.window_state, self.change_widgets)

	def _display_widets(self, state, change):
		"""widget organizer"""
		#### NEED TO ORGANIZE THE DIFFERENT WINDOWS STATES ####
		if state == 0:
			self._url_entry_box()
			self._enter_button(self._entry_button_function)
		elif state == 1:
			self._stream_options_listbox()
			self._enter_button(self._listbox_button_function)
		elif state == 2:
			self._streams_listbox()
			self._enter_button(self._listbox_button_function)

	def _enter_button(self, buttoncommand):
		"""initial enter button"""
		self.enter_button = tk.Button(self.master, text="Enter", command=buttoncommand)
		#self.enter_button.bind("<Button-1>", self.button_function())
		self.enter_button.pack(pady=20)

	def _listbox_button_function(self):
		"""function for the button to grab the listbox focus"""
		if self.stream_options_list_box != None:
			self.user_selection = self.stream_options_list_box.curselection()
		elif self.stream_list_box != None:
			self.user_selection = self.stream_list_box.curselection()

	def _entry_button_function(self):
		"""get and check user input"""
		self.initial_user_input = self.entry_box.get()
		if self.input_check.url_text_check(self.initial_user_input):
			# if the user input is indeed a youtube url we want to get the streams
			self.down_load.videotube(self.initial_user_input)

	def _destroy_widgets(self):
			# disable video url entry field
			self.entry_box.destroy()
			# destroy url entry button
			self.enter_button.destroy()
			# destroy steam listbox
			self.stream_list_box.destroy()
			#destroy stream options list box
			self.stream_options_list_box.destroy()
			# change the state
			self.window_state += 1

		
	def _streams_listbox(self):
		"""take and display the stream options for a url"""
		# stream list 
		self.stream_list = self.down_load.streamList
		self.stream_list_box = tk.Listbox(self.master, width=30)
		self.stream_list_box.pack(pady=20)
		for i in enumerate(self.stream_list):
			# insert takes index and string 
			self.stream_list_box.insert(0, i)
	
	def _stream_options_listbox(self):
		"""display the stream options"""
		self.stream_options_list_box = tk.Listbox(self.master, width=30)
		self.stream_options_list_box.pack(pady=20)
		self.stream_options_list_box.insert(0, "Audio only")
		self.stream_options_list_box.insert(1, "Video only")
		self.stream_options_list_box.insert(2, "Both")

	def _url_entry_box(self):
		"""entry box for user url"""
		self.entry_box = tk.Entry(self.master, )
		self.entry_box.pack(pady=20)

	

if __name__ == '__main__':
	window = VideoDownloader(root)
	root.mainloop()
