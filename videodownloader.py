import tkinter as tk
from input_check import Input_Check
from down_load import Down_Load

root = tk.Tk()
root.title("Chaes' video downloader ")
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
        self.down_load = Down_Load(self, self.input_check)
        self.master = master
        # window manager variables
        self.window_state = 0
        self.change_widgets = False
        # tk.OptionsMenu(master, func, *list, command=#command)
        self._display_widets(self.window_state)

    def _display_widets(self, state):
        """ window and widget organizer """
        # take a youtube url
        if state == 0:
            # get users youtube url
            self._display_state_one()
        elif state == 1:
            # get users download option
            self._display_state_two()
        elif state == 2:
            self._display_state_three()
        elif state == 3:
            self._display_state_four()

    def _display_state_one(self):
        """ ask the user to enter a youtube video url """
        directionstext = "Enter a Youtube URL."
        self._text_label(directionstext)
        self._url_entry_box()
        self._enter_button(self._entry_button_function)

    def _display_state_two(self):
        """ ask the user to select download option """
        directionstext = "Select download option."
        self._text_label(directionstext)
        self._stream_type_options_listbox()
        self._enter_button(self._select_type_option_function)

    def _display_state_three(self):
        """ take the user format choice """
        directionstext = "Select format"
        formatlist = ["webm", "mp4"]
        self._text_label(directionstext)
        self._create_options_listbox(formatlist)
        self._enter_button(self._select_format_function)

    def _display_state_four(self):
        """ ask the user to select an available resolution """
        directionstext = "Select an available resolution"
        self._text_label(directionstext)
        self._create_options_listbox(self.down_load.user_video_available_resolutions)
        self._enter_button(self._select_resolution_function)
    

    def _text_label(self, directionstext):
        """ display text for the user """
        self.text_label = tk.Label(text=directionstext)
        self.text_label.pack(pady=20)

    def _enter_button(self, buttoncommand):
        """ initial enter button """
        self.enter_button = tk.Button(
            self.master, text="Enter", command=buttoncommand)
        self.enter_button.pack(pady=20)

    def _select_format_function(self):
        """ select format enter button funciton """
        user_selection = self.stream_options_list_box.curselection()
        print(user_selection)
        filtered_list = []
        # if  user selects webm
        if user_selection[0] == 0:
            print("webm selected")
            for stream in self.input_check.stream_format(self.down_load.streamList, "webm"):
                filtered_list.append(stream)
        # if user selects mp4
        elif user_selection[0] == 1:
            print("mp4 selected")
            for stream in self.input_check.stream_format(self.down_load.streamList, "mp4"):
                filtered_list.append(stream)
        self.down_load.streamList = filtered_list
        for laStream in self.down_load.streamList:
            print(laStream)
        self._destroy_widgets(self.window_state)
        self._display_widets(self.window_state)

    def _select_resolution_function(self):
        """ select resolution enter button function """
        user_selection = self.stream_options_list_box.curselection()
        print(f"User selected: {user_selection[0]}")
        print(f"The resolution selected = {self.down_load.user_video_available_resolutions[int(user_selection[0])]}")
        # user selection is matching the index 
        for i in self.down_load.user_video_available_resolutions:
            if user_selection[0] == i:
                filtered_list = self.input_check.one_resolution_only(self.down_load.streamList, user_selection[0])

        #self.down_load.streamList = filtered_list
        self._destroy_widgets(self.window_state)
        self._create_options_listbox(filtered_list)

    def _select_type_option_function(self):
        """ select option from listbox """
        # select the user video download option
        user_selection = self.stream_options_list_box.curselection()
        print(user_selection[0])
        # Video and audio = 0
        if user_selection[0] == 0:
            filtered_list = self.input_check.video_audio(
                self.down_load.streamList)
        # Video only = 1
        elif user_selection[0] == 1:
            filtered_list = self.input_check.video_only(
                self.down_load.streamList)
        # Audio only = 2
        elif user_selection[0] == 2:
            filtered_list = self.input_check.audio_only(
                self.down_load.streamList)
        print(filtered_list)
        self._destroy_widgets(self.window_state)
        self._display_widets(self.window_state)
        return filtered_list

    def _select_stream_function(self):
        """ function to grab the selected stream and download it """
        # user picking the actual stream they want
        self.user_selection = self.stream_list_box.curselection()
        # need to add self.down_load.select_stream

    def _entry_button_function(self):
        """get and check user input"""
        self.initial_user_input = self.entry_box.get()
        if self.input_check.url_text_check(self.initial_user_input):
            # if the user input is indeed a youtube url we want to get the streams
            self.down_load.videotube(self.initial_user_input)
            # destroy the widgets and change thw window state number
            self._destroy_widgets(self.window_state)
            self._display_widets(self.window_state)
            for res in self.down_load.user_video_available_resolutions:
                print(res)

    def _destroy_widgets(self, state):
        """ the one ring """
        if state == 0:
            # destroy text
            self.text_label.destroy()
            # disable video url entry field
            self.entry_box.destroy()
            # destroy url entry button
            self.enter_button.destroy()
        elif state == 1:
            self.text_label.destroy()
            # destroy stream options list box
            self.stream_options_list_box.destroy()
            self.enter_button.destroy()
        elif state == 2:
            self.text_label.destroy()
            # destroy steam listbox
            self.stream_options_list_box.destroy()
            self.enter_button.destroy()
            # change the state
        self.window_state += 1

    def _available_resolutions_listbox(self):
        """ take and display available resolutions """
        self.available_resolutions_list_box = tk.Listbox(self.master, width=30)
        self.available_resolutions_list_box.pack(pady=20)
        for i in enumerate(self.down_load.user_video_available_resolutions):
            self.available_resolutions_list_box.insert(0, i)

    def _streams_listbox(self):
        """ take and display the stream options for a url """
        # stream list
        self.stream_list = self.down_load.streamList
        self.stream_list_box = tk.Listbox(self.master, width=30)
        self.stream_list_box.pack(pady=20)
        for i in enumerate(self.stream_list):
            # insert takes index and string
            self.stream_list_box.insert(0, i)

    def _stream_type_options_listbox(self):
        """ display the stream options """
        self.stream_options_list_box = tk.Listbox(self.master, width=30)
        self.stream_options_list_box.pack(pady=20)
        self.stream_options_list_box.insert(0, "Video with audio")
        self.stream_options_list_box.insert(1, "Video only")
        self.stream_options_list_box.insert(2, "Audio only")

    def _create_options_listbox(self, optionslist):
        """ display resolution options """
        self.stream_options_list_box = tk.Listbox(self.master, width=30)
        self.stream_options_list_box.pack(pady=20)
        for num, ting in enumerate(optionslist):
            self.stream_options_list_box.insert(num, ting)

    def _url_entry_box(self):
        """ entry box for user url """
        self.entry_box = tk.Entry(self.master, )
        self.entry_box.pack(pady=20)


if __name__ == '__main__':
    window = VideoDownloader(root)
    root.mainloop()
