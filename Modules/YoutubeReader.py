import urllib.request, pygame, vlc, pafy, re, pygame, unicodedata, requests

class YoutubeReader:
    def __init__(self):
        self.inst = vlc.Instance()
        self.player = self.inst.media_player_new()
        self.Readable = False

    def SearchVideo(self, search):
        searchWords = str(unicodedata.normalize('NFD', str(re.sub(" ", "+", search))).encode('ascii', 'ignore'))
        searchResponse = urllib.request.urlopen("https://www.youtube.com/results?search_query="+searchWords)
        searchResults = re.findall('href=\"\\/watch\\?v=(.{11})', searchResponse.read().decode())
        url = 'https://www.youtube.com/watch?v='+searchResults[0]
        self.id = searchResults[0]
        return pafy.new(url).getbestaudio().url

    def ReadVideo(self, videoURL):
        if self.Readable:
            self.StopVideo()
        Media = self.inst.media_new(videoURL)
        Media.get_mrl()
        self.player.set_media(Media)
        self.player.play()
        self.Readable = True

    def PlayPauseVideo(self):
        if self.Readable:
            self.player.pause()
        else:
            return None

    def SaveMiniature(self):
        urllib.request.urlretrieve('https://img.youtube.com/vi/'+self.id+'/hqdefault.jpg', "./Ressources/Minia.jpg")
        return True

    def GetTitle(self):
        request = requests.get('https://www.youtube.com/oembed?url=http%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3D'+self.id+'&format=json').json()
        return str(request['title'])

    def StopVideo(self):
        if self.Readable:
            self.player.stop()
            self.Readable = False
        else:
            return None

    def IsFinished(self):
        result = False
        if self.player.get_state() == vlc.State.Ended:
            result = True
        else:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    result = True
        return result
