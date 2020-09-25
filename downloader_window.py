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
            print("2. Filter streams.")
            user_selection = input("? ")
            if int(user_selection) in range(1, 3):
                return int(user_selection)
            elif user_selection.lower() == 'exit':
                sys.exit()
            else:
                print(colored("Invalid input.", "red"))
                print("Try again.")
                continue

    def Resolution_selection(self, userselection):
        ''' Filter streams by resolution
        '''
        pass

    def Filter_Streams_Menu(self, streamslist):
        ''' Menu to allow the user to filter the video streams 
        '''
        streams_list = streamslist
        while True:
            print("Select a filter")
            print("1. Resolution")
            print("2. Format")
            print("3. FPS")
            print("4. Video and audio together only")
            print("5. Video only")
            print("6. Audio only")
            user_selection = input("? ")
            # if the input is valid
            if int(user_selection) in range(1, 7):
                # execute the users selection
                if int(user_selection) == 1:
                    available_resolutions = self.filter_streams.available_resolutions(
                        streams_list)
                    print("Available resolutions")
                    for i in available_resolutions:
                        print(i)

            else:
                print(colored("Invalid input.", "red"))
                continue

    def run_program(self):
        ''' main organizer for the program
        '''
        user_url = self.intro()
        streams_list = self.downloader.videotube(user_url)
        user_menu_selection = self.Main_Menu()

        if user_menu_selection == 1:
            for i in streams_list:
                print(i)

        # TODO: Add filter streams functionality


if __name__ == '__main__':
    video_downloader = Video_Downloader()
    video_downloader.run_program()
