from Modules.FaceRecoThread import FaceRecog
import time
class FaceReco:
    def __init__(self):
        self.possible = True
        self.Reco = FaceRecog()
        if self.Reco.start() == 'Unknown':
            print('Impossible')
            self.possible = False

    def Get_Xpos(self):
        if self.Reco.free:
            return -(self.Reco.results[0]/260)
        else:
            return 0

    def Get_Ypos(self):
        if self.Reco.free:
            return self.Reco.results[1]/180
        else:
            return 0

    def GetPerson(self):
        if self.Reco.Face:
            return True

    def Pause(self):
        self.Reco.Face = 'Wait'

    def Play(self):
        self.Reco.Face = False

    def Shutdown(self):
        self.Reco.Run = False
        return True