import tkinter as tk
from input_check import Input_Check

root = tk.Tk()
root.title("Chae's video downloader ")
# root.iconbitmap()
root.geometry("400x400")

class VideoDownloader:
	"""Video downloader class"""

	def __init__(self, master=None):
		"""init downloader variables"""
		self.frame = tk.Frame(master)
		self.frame.pack()

		self.input_check = Input_Check()

		# tk.OptionsMenu(master, func, *list, command=#command)

	def enter_button(self):	

		self.enter_button = tk.Button(master, text="Enter", command=#command)
		self.enter_button.bind("<Button-1>", #check the text input for url command)
		self.enter_button.pack(pady=20)

	def streams_list(self):
		"""take and display the stream options for a url"""
		
	

if __name__ == '__main__':
	window = VideoDownloader(root)
	root.mainloop()
