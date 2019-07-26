from Modules.Screen import Screen
from Modules.Sound import Sound
import time

# Création écran + Son
ecran = Screen(1280, 720)
son = Sound()
OfflineMode = False

# Initialisation
time.sleep(1)
son.Play_TurnOn()
time.sleep(0.2)
ecran.Refresh()
ecran.CreateStartLogo('startlogo', 270, 100, 150)
time.sleep(1)
ecran.CreateLoading('loading', 350, 475, 930, 485)

# Chargement des modules
son.LoadAll()
from Modules.Yeelight import Lampe
lampe = Lampe()
if lampe.Offline:
    OfflineMode = True
from Modules.Weather import Weather
temp = Weather()
from Modules.Weather import Weather
meteo = Weather()
from Modules.SpeechToText import SpeechToText
recovoc = SpeechToText()
import re
from Modules.YoutubeReader import YoutubeReader
Youtube = YoutubeReader()

# Fin des animations
ecran.Delete('startlogo')
ecran.Delete('loading')

MainRun = True
# Code
ecran.CreateFace('Face')
Face = ecran.GetObject('Face')
SongState = [False, False]
#          loaded  played

while MainRun:
    if son.IsKeyWord():
        command = False
        Face.Pause()
        son.Play_RecordOn()
        volume = Youtube.player.audio_get_volume()
        Youtube.player.audio_set_volume(int(Youtube.player.audio_get_volume()/2))
        ecran.CreateListenRect('listenrect')
        record = recovoc.ListenCommand()
        son.Play_RecordOff()
        ecran.Delete('listenrect')
        Youtube.player.audio_set_volume(volume)
        message = recovoc.Recognize(record).lower()
        print('Tu as dit: '+message)

        if re.search('allume.*(lampe|lumière).*', message):
            lampe.Turn_On()
            son.Say("J'ai allumé la lampe.")
            
        if re.search('(mes|mets) la.* à .*', message):
            fait = False
            value = 100
            for word in message.split(' '):
                try:
                    test = int(word)
                    value = test
                    fait = True
                except:
                    fait = False
            lampe.Bright(value)
            son.Say("J'ai mis la lampe à "+str(value)+' pourcent.')

        if re.search('.*(mes|mets).*', message) and re.search('.*(lampe|lumière).*', message):
            for value in message.split(' '):
                if value == 'rouge':
                    lampe.Color_Red()
                    son.Say("J'ai mis la lampe en rouge.")
                if value == 'verre' or value == 'vert':
                    lampe.Color_Green()
                    son.Say("J'ai mis la lampe en vert.")
                if value == 'bleu' or value == 'bleue':
                    lampe.Color_Blue()
                    son.Say("J'ai mis la lampe en bleu.")
                if value == 'blanc' or value == 'blanche':
                    lampe.Color_White()
                    son.Say("J'ai mis la lampe en blanc.")
                if value == 'chaud' or value == 'chaude':
                    lampe.Color_Hot()
                    son.Say("J'ai mis la lampe en couleur chaude.")
                if value == 'froid' or value == 'froide':
                    lampe.Color_Cold()
                    son.Say("J'ai mis la lampe en couleur froide.")

        if re.search('.*éteins.*(lampe|lumière).*', message):
            lampe.Turn_Off()
            son.Say("J'ai éteins la lampe.")

        if re.search('.*(temp|météo).*', message):
            ville = 'Manonville'
            index = 0
            for word in message.split(' '):
                if word == 'à' or word == 'de':
                    try:
                        ville = message.split(' ')[index+1]
                    except:
                        ville = 'Manonville'
                index += 1
            print(ville)
            temperature = str(meteo.Temperature(ville))
            typeTemp = meteo.TypeTemp(ville)
            if temp and typeTemp:
                son.Say('À '+ville+", il fait "+temperature+" degrés. Et il y a "+typeTemp)

        if re.search('(mes|mets).*(volume|musique).*', message) and re.search('.*à.*', message):
            fait = False
            value = 100
            for word in message.split(' '):
                try:
                    test = int(word)
                    if -1 < test < 101:
                        value = test
                        fait = True
                except:
                    fait = False
            Youtube.player.audio_set_volume(value)
            son.Say("J'ai mis le volume à "+str(value)+' pourcent.')

        
        if re.search('(mes|mets).*youtube.*', message):
            search = " ".join(re.search('(mes|mets).*youtube', message).group().split(' ')[1:-2])
            print(search)
            son.Say('Ok, je met '+search+' sur YouTube.')
            if SongState[0]:
                Youtube.StopVideo()
                ecran.Delete('ytpic')
                ecran.Delete('yttitle')
            try:
                url = Youtube.SearchVideo(search)
                Youtube.SaveMiniature()
                Youtube.ReadVideo(url)
                Face.Hide()
                ecran.CreateYTpicture('ytpic')
                ecran.CreateYTtitle('yttitle', Youtube.GetTitle())
                SongState = [True, True]
            except AttributeError:
                son.Say("Désolé, je n'ai pas trouvé cette fois ...")

        if re.search('.*arrête.*musique.*', message):
            Youtube.StopVideo()
            ecran.Delete('ytpic')
            ecran.Delete('yttitle')
            Face.Show()
            son.Say("D'accord, j'arrête la musique")
            SongState[0] = False
            command = True

        if re.search('.*play.*', message):
            if not SongState[1]:
                Youtube.PlayPauseVideo()
                SongState[1] = True
                son.Say("J'ai mis sur play")

        if re.search('.*pause.*', message):
            if SongState[1]:
                Youtube.PlayPauseVideo()
                SongState[1] = False
                son.Say("J'ai mis sur pause")
            command = True

        if re.search('.*ça va.*', message):
            son.Say("Oui ! Je viens même de faire une tourte !")
            time.sleep(1)
            son.Say("Euh... Attends ... Quel parfum ?")
            time.sleep(1)
            son.Say("AH OUI ! parfum tourte !")

        if re.search('(non|rien)+', message):
            son.Say("Ah d'accord")

        if re.search('.*voix.*', message):
            if re.search('google', message):
                son.Set_TTS('Google')
                son.Say("D'accord, je prend la voix de Google.")
            if re.search('autre', message):
                son.Set_TTS('Espeak')
                son.Say("D'accord, je prend la voix Offline.")

        if re.search('(arrête|éteins)-toi', message):
            MainRun = False
            son.Say("Ok, je m'éteins")

        son.ResetCommand()
        Face.Play()

    if Face.IsPerson():
        Face.SetFace('normal')
    else:
        Face.SetFace('sleeping')
    time.sleep(0.1)

ecran.Delete('Face')
# Shutdown de Flow
son.Shutdown()
ecran.ShutDown()
