import tkinter as tk
from input_check import Input_Check

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

		self.master = master

		# tk.OptionsMenu(master, func, *list, command=#command)

		# stream list 
		self.stream_list = ["stream one", "stream two", "stream three"]

		self.url_entry_box()
		self.enter_button()

	def enter_button(self):

		self.enter_button = tk.Button(self.master, text="Enter", command=self.button_function)
		#self.enter_button.bind("<Button-1>", self.button_function())
		self.enter_button.pack(pady=20)

	def button_function(self):
		"""get and check user input"""
		self.initial_user_input = self.entry_box.get()
		if self.input_check.url_text_check(self.initial_user_input):
			# if the user input is indeed a youtube url we want to get the streams 
			print("Function has worked!")
			return True

	def print_streams_list(self):
		print(self.stream_list)
		
	def streams_listbox(self):
		"""take and display the stream options for a url"""
		sl = tk.Listbox(self.master, )
		for i in self.stream_list:
			sl.activate(i)

	def url_entry_box(self):
		"""box that the user enters the url into"""
		self.entry_box = tk.Entry(self.master, )
		self.entry_box.pack(pady=20)

	

if __name__ == '__main__':
	window = VideoDownloader(root)
	root.mainloop()
