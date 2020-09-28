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

    def intro(self):
        ''' Start of the program
        '''
        while True:
            print("")
            print("Welcome to Chae's Video Downloader!\n")
            print(colored("Enter 'exit' at anytime to quit the program.", "blue"))
            print("")
            user_url = input("Enter a YouTube url: ")
            if user_url.lower() == 'exit':
                sys.exit()
            elif self.filter_streams.url_text_check(user_url):
                return user_url
            else:
                print(colored("Invalid input.", "red"))
                continue

    def Main_Menu(self):
        ''' Programs main menu
        '''
        while True:
            print("Select an option\n")
            print("1. Show available streams.")
            print("2. Select a stream.")
            user_selection = input("? ")
            if int(user_selection) in range(1, 3):
                return int(user_selection)
            elif user_selection.lower() == 'exit':
                sys.exit()
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
        available_resolutions.sort()
        print("Select a resolution")
        for num, res in enumerate(available_resolutions):
            print(f"{num}. {res}")
        resolution_selection = input("? ")
        if self.filter_streams.check_if_resolution.search(available_resolutions[int(resolution_selection)]):
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
            Outputs new index list of only the formats the user wants
        '''
        stream_index_list = indexlist
        streams_list = list(streamslist)
        print("Select a format.")
        print("1. mp4")
        print("2. webm")
        user_selection = input("? ")

        if user_selection.lower() != 'exit':
            if int(user_selection) == 1:
                stream_index_list = self.filter_streams.format_filter(
                    streams_list, indexlist, 'mp4')
            elif int(user_selection) == 2:
                stream_index_list = self.filter_streams.format_filter(
                    streams_list, indexlist, 'webm')
        else:
            print(colored("Invalid input.", "red"))

        return stream_index_list

    def Filter_Streams_Menu(self, streamslist):
        ''' Menu to allow the user to filter the video streams
        '''
        streamslist = list(streamslist)

        # Grab users desired resolution
        users_stream_index_list = self.Resolution_selection(streamslist)
        # Grab users desired format
        users_stream_index_list = self.Format_selection(
            streamslist, users_stream_index_list)

    def run_program(self):
        ''' main organizer for the program
        '''
        user_url = self.intro()
        streams_list = self.downloader.videotube(user_url)
        user_menu_selection = self.Main_Menu()

        if user_menu_selection == 1:
            for i in streams_list:
                print(i)
        else:
            self.Filter_Streams_Menu(streams_list)


if __name__ == '__main__':
    video_downloader = Video_Downloader()
    video_downloader.run_program()
