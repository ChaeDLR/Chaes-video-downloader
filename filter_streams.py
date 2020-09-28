import re


class Filter_Streams:
    """inputclass"""

    def __init__(self):
        """init for this test"""
        self.url_match = False
        self.youtube_check = re.compile(r'youtube.com/watch')
        self.audio_only_check = re.compile(r'acodec')
        self.video_only_check = re.compile(r'vcodec')
        self.both_video_audio_check = re.compile(r'False')
        self.webm_format_check = re.compile(r'webm')
        self.mp4_format_check = re.compile(r'mp4')
        # identify resolutions from a stream object
        self.check_for_resolution = re.compile(r'res="(\d\d\d\d?)p"')
        # check if a user input is a resolution
        self.check_if_resolution = re.compile(r'(\d\d\d\d?)p')

        # resolutions
        self.check_for_1440p = re.compile(r'res="1440p"')
        self.check_for_1080p = re.compile(r'res="1080p"')
        self.check_for_720p = re.compile(r'res="720p"')
        self.check_for_480p = re.compile(r'res="480p"')
        self.check_for_360p = re.compile(r'res="360p"')
        self.check_for_240p = re.compile(r'res="240p"')
        self.check_for_144p = re.compile(r'res="144p"')

    def available_resolutions(self, streamlist):
        """ take the streamlist and output available resolutions in a list """
        stream_list = self.check_for_resolution.findall(str(streamlist))
        available_resolutions_list = []
        for stream in stream_list:
            available_resolutions_list.append(f'{stream}p')
        available_resolutions_list = list(
            dict.fromkeys(available_resolutions_list))
        return available_resolutions_list

    def stream_format(self, streamlist, formatchoice):
        """ return stream format choice index """
        filtered_list = []
        if formatchoice == "webm":
            for stream in streamlist:
                if self.webm_format_check.search(str(stream)):
                    filtered_list.append(stream)
            return filtered_list
        elif formatchoice == "mp4":
            for stream in streamlist:
                if self.mp4_format_check.search(str(stream)):
                    filtered_list.append(stream)
            return filtered_list

    def url_text_check(self, textstring):
        """ check that a string is a youtube.com/watch url """
        isYoutubeUrl = self.youtube_check.search(textstring)
        if isYoutubeUrl:
            print("URl passed check")
            return True

    def format_filter(self, streamlist, indexlist, userformat):
        """ take in the current stream list and filter out anything not webm """
        indexes_list = []
        if userformat == 'mp4':
            for index in indexlist:
                if self.mp4_format_check.search(str(streamlist[index])):
                    indexes_list.append(index)
        elif userformat == 'webm':
            for index in indexlist:
                if self.webm_format_check.search(str(streamlist[index])):
                    indexes_list.append(index)

        return indexes_list

    def resolution_selection_index(self, streamlist, resolution):
        """ take stream list and output list with resolution option only """
        index_list = []
        resolution_regex = self.choose_resolution_regex(resolution)
        for num, stream in enumerate(streamlist):
            if resolution_regex.search(str(stream)):
                index_list.append(num)
        #one_res_streams_list = list(dict.fromkeys(one_res_streams_list))
        return index_list

    def choose_resolution_regex(self, resolution):
        ''' Take the desired resolution
            Return desired regex
        '''
        if resolution == '1440p':
            return self.check_for_1440p
        elif resolution == '1080p':
            return self.check_for_1080p
        elif resolution == '720p':
            return self.check_for_720p
        elif resolution == '480p':
            return self.check_for_480p
        elif resolution == '360p':
            return self.check_for_360p
        elif resolution == '240p':
            return self.check_for_240p
        elif resolution == '144p':
            return self.check_for_144p
        else:
            print("Invalid input in choose_resolution_regex")

    def audio_only(self, streamlist):
        """ take stream list and output list of audio streams only """
        audio_only_streams_list = []
        # loop through the streamlist
        for _, stream in enumerate(streamlist):
            audio_only_stream = self.audio_only_check.search(str(stream))
            if audio_only_stream != None:
                audio_only_streams_list.append(stream)
        return audio_only_streams_list

    def video_only(self, streamlist):
        """ take stream list and output list of video streams only """
        video_only_streams_list = []
        # loop through the streamlist
        for _, stream in enumerate(streamlist):
            video_only_stream = self.video_only_check.search(str(stream))
            if video_only_stream != None:
                video_only_streams_list.append(stream)
        return video_only_streams_list

    def video_audio(self, streamlist):
        """ take stream list and remove the audio and video only streams """
        video_audio_streams_list = []
        # loop through the streamlist
        for _, stream in enumerate(streamlist):
            video_audio_stream = self.both_video_audio_check.search(
                str(stream))
            if video_audio_stream != None:
                video_audio_streams_list.append(stream)
        return video_audio_streams_list
