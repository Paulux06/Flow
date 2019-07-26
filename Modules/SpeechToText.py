import speech_recognition as sr

class SpeechToText:
    def __init__(self):
        self.Recognizer = sr.Recognizer()
        self.Audio = None
        #with sr.Microphone() as source:
        #    print('Ajustement du bruit...')
        #    self.Recognizer.adjust_for_ambient_noise(source)
        self.AdjustAmbientNoise()
        

    def ListenCommand(self):
        with sr.Microphone() as source:
            print('Écoute en cours ...')
            self.Audio = self.Recognizer.listen(source)
            return self.Audio
            
    def Recognize(self, audio):
        print('Reconnaissance en cours ...')
        try:
            Message = self.Recognizer.recognize_google(audio, language='fr_FR')
            return Message            
        except sr.UnknownValueError:
            return 'Pas compris ...'
        except sr.RequestError:
            return 'Error'
    
    def AdjustAmbientNoise(self):
        print('Ajustement ...')
        with sr.Microphone() as source:
            self.Recognizer.dynamic_energy_threshold = True
            self.Recognizer.adjust_for_ambient_noise(source)
            print('Threshold:\n'+str(self.Recognizer.energy_threshold))
            self.Recognizer.dynamic_energy_threshold = False
            self.Recognizer.energy_threshold += 500
        print('Fini')