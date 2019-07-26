import pygame
from pydub import AudioSegment
from gtts import gTTS
failed = False
from Modules.AudioDetection import AudioDetection

class Sound:
    def __init__(self):
        pygame.mixer.init()
        self.Turn_On = pygame.mixer.Sound('./Ressources/On.wav')
        self.Ready = True
        self.AudioDetect = AudioDetection()
        self.AudioDetect.start()
        import pyttsx3 
        self.engine = pyttsx3.init() 
        voice = self.engine.getProperty('voices')[26].id
        self.engine
        self.engine.setProperty('voice', voice)
        self.engine.setProperty('rate', 160)
        self.tts = 'Espeak'

    def Set_TTS(self, Name):
        if Name == 'Google' or Name == 'Espeak':
            self.tts = Name
        else:
            return False

    def Play_TurnOn(self):
        pygame.mixer.Sound.play(self.Turn_On)

    def LoadAll(self):
        self.Turn_On = pygame.mixer.Sound('./Ressources/On.wav')
        self.Turn_Off = pygame.mixer.Sound('./Ressources/Off.wav')
        self.Record_On = pygame.mixer.Sound('./Ressources/Record_On.wav')
        self.Record_Off = pygame.mixer.Sound('./Ressources/Record_Off.wav')
        self.Menu_Close = pygame.mixer.Sound('./Ressources/Menu_Close.wav')
        self.Menu_Open = pygame.mixer.Sound('./Ressources/Menu_Open.wav')
        self.Menu_Select = pygame.mixer.Sound('./Ressources/Menu_Select.wav')
        self.Menu_Swipe = pygame.mixer.Sound('./Ressources/Menu_Swipe.wav')

    def Play_TurnOff(self):
        pygame.mixer.Sound.play(self.Turn_Off)

    def Play_RecordOn(self):
        pygame.mixer.Sound.play(self.Record_On)

    def Play_RecordOff(self):
        pygame.mixer.Sound.play(self.Record_Off)

    def Play_MenuClose(self):
        pygame.mixer.Sound.play(self.Menu_Close)

    def Play_MenuOpen(self):
        pygame.mixer.Sound.play(self.Menu_Open)

    def Play_MenuSelect(self):
        pygame.mixer.Sound.play(self.Menu_Select)

    def Play_MenuSwipe(self):
        pygame.mixer.Sound.play(self.Menu_Swipe)

    def Say(self, sentence):
        if self.tts == 'Espeak':
            self.engine.say(sentence) 
            self.engine.runAndWait()
        if self.tts == 'Google':
            gTTS(text=sentence, lang='fr', slow=False).save('./Ressources/TextToSpeech.mp3')
            AudioSegment.from_mp3("./Ressources/TextToSpeech.mp3").export("./Ressources/TextToSpeech.wav", format="wav")
            pygame.mixer.Sound('./Ressources/TextToSpeech.wav').play()

    def IsKeyWord(self):
        if self.AudioDetect.CommandFound == 'True':
            self.AudioDetect.CommandFound = 'Wait'
            return True

    def ResetCommand(self):
            self.AudioDetect.CommandFound = 'False'
            return True

    def Shutdown(self):
        self.AudioDetect.Shutdown()