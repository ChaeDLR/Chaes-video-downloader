import sys
from termcolor import colored
from down_load import Down_Load
from filter_streams import Filter_Streams


class Video_Downloader:
    ''' Program console manager class
    '''

    def __init__(self):
        ''' Initialize ui window
        '''
        self.downloader = Down_Load()
        self.filter_streams = Filter_Streams()

    def greeting(self):
        ''' Start of the program
        '''
        print("")
        print("Welcome to Chae's Video Downloader!\n")
        print(colored("Enter 'exit' at anytime to quit the program.", "blue"))
        print("")

    def Main_Menu(self):
        ''' Programs main menu
        '''
        while True:
            print("Select an option\n")
            print("1. Show available streams.")
            print("2. Select a stream.")
            user_selection = input("? ")
            if user_selection.lower() == 'exit':
                break
            elif int(user_selection) in range(1, 3):
                return int(user_selection)
            else:
                print(colored("Invalid input.", "red"))
                print("Try again.")
                continue

    def Resolution_selection(self, streamslist):
        ''' Takes the streams list
            Asks user what resolution they want
            Returns list of the indexes that match the resolution
        '''
        streams_list = list(streamslist)
        available_resolutions = self.filter_streams.available_resolutions(
            streams_list)
        print("Select a resolution")
        for num, res in enumerate(available_resolutions):
            print(f"{num}. {res}p")
        resolution_selection = input("? ")
        if self.filter_streams.check_if_resolution.search(str(available_resolutions[int(resolution_selection)])):
            resolution_selection = available_resolutions[int(
                resolution_selection)]
            print(f"Resolution selection {resolution_selection}")
            streams_list_resolution_indexes = self.filter_streams.resolution_selection_index(
                streams_list, resolution_selection)
            return streams_list_resolution_indexes
        elif resolution_selection.lower() == 'exit':
            sys.exit()
        else:
            print(colored("Invalid input.", "red"))

    def Format_selection(self, streamslist, indexlist):
        ''' Takes the streamlist and indexes to work with
            Ask user their desirec format
            Outputs new index list of only the formats the user wants
        '''
        stream_index_list = indexlist
        streams_list = list(streamslist)
        print("Select a format.")
        print("1. mp4")
        print("2. webm")
        user_selection = input("? ")

        if user_selection.lower() == 'exit':
            sys.exit()
        elif int(user_selection) in range(1, 3):
            if int(user_selection) == 1:
                stream_index_list = self.filter_streams.format_filter(
                    streams_list, indexlist, 'mp4')
            elif int(user_selection) == 2:
                stream_index_list = self.filter_streams.format_filter(
                    streams_list, indexlist, 'webm')
        else:
            print(colored("Invalid input.", "red"))

        return stream_index_list

    def Fps_selection(self, streamslist, indexlist):
        ''' Takes streamslist and indexes
            Ask user what fps they want
            Output index of stream
        '''
        stream_index_list = indexlist
        streams_list = list(streamslist)
        print("Select an fps.")
        print("1. 60")
        print("2. 30")
        user_selection = input("? ")

        if user_selection.lower() == 'exit':
            sys.exit()
        elif int(user_selection) in range(1, 3):
            if int(user_selection) == 1:
                stream_index = self.filter_streams.Fps_index_selection(
                    streams_list, stream_index_list, '60fps')
                return stream_index
            elif int(user_selection) == 2:
                stream_index = self.filter_streams.Fps_index_selection(
                    streams_list, stream_index_list, '30fps')
                return stream_index
        else:
            print(colored("Invalid input.", "red"))

    def Filter_Streams_Menu(self, streamslist):
        ''' Menu to allow the user to filter the video streams
        '''
        webm = False
        mp4 = False
        streamslist = list(streamslist)
        users_stream_index_list = self.Resolution_selection(streamslist)
        for index in users_stream_index_list:
            if self.filter_streams.webm_format_check.search(str(streamslist[index])):
                webm = True
            elif self.filter_streams.mp4_format_check.search(str(streamslist[index])):
                mp4 = True
                # need to check if there are more than one format for the stream here
        if webm & mp4:
            users_stream_index_list = self.Format_selection(
                streamslist, users_stream_index_list)
        else:
            for index in users_stream_index_list:
                print(streamslist[index])

        if len(users_stream_index_list) > 1:
            stream_index = self.Fps_selection(
                streamslist, users_stream_index_list)
        else:
            stream_index = users_stream_index_list[0]

        print("Downloading video...")
        self.downloader.select_stream(stream_index)
        print(f"Finished downloading stream {streamslist[stream_index]}")

    def Intro(self):
        ''' Ask user for a url
            Decides the video to be worked with
        '''
        while True:
            user_url = input("Enter a YouTube url: ")
            if user_url.lower() == 'exit':
                sys.exit()
            elif self.filter_streams.url_text_check(user_url):
                streams_list = self.downloader.videotube(user_url)
                break
            else:
                print("Url error.")
                continue
        return streams_list

    def Streams_menu(self, streamlist):
        ''' Menu that allows user to work with streams
        '''
        streams_list = streamlist
        while True:
            user_menu_selection = self.Main_Menu()
            if user_menu_selection == 1:
                for i in streams_list:
                    print(i)
            elif user_menu_selection == 2:
                self.Filter_Streams_Menu(streams_list)
                break
            elif str(user_menu_selection).lower() == 'exit':
                sys.exit()
            else:
                print(colored("Invalid input.", "red"))
                continue

    def run_program(self):
        ''' main organizer for the program
        '''
        self.greeting()
        streams_list = self.Intro()
        self.Streams_menu(streams_list)


if __name__ == '__main__':
    video_downloader = Video_Downloader()
    video_downloader.run_program()
