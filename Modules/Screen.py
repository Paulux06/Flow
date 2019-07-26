import pygame
from Modules.ScreenObjects import Loading, StartLogo, Text, Face, ListenRect, YTtext, YTpicture
from Modules.Refresher import Refresher

class Screen:
    def __init__(self, width, height):
        pygame.init()
        self.objets = []
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption('Flow')
        pygame.display.set_icon(pygame.image.load('./Ressources/Flow_Logo.png'))
        #pygame.display.toggle_fullscreen()
        pygame.mouse.set_visible(False)
        self.font = pygame.font.SysFont('sansserif', 16)
        Clock = pygame.time.Clock()
        Clock.tick(10)

    def Refresh(self):
        self.thrd = Refresher(self.screen, self.objets)
        self.thrd.start()

    def DispObjets(self):
        print(self.objets)

    def CreateLoading(self, Name, Xmin, Ymin, Xmax, Ymax):
        self.possible = True
        for objet in self.objets:
            if objet.name == Name:
                print('existe deja')
                self.possible = False
        if self.possible:
            self.objets.append(Loading(Name, Xmin, Ymin, Xmax, Ymax))
            
    def CreateStartLogo(self, Name, Ystart, Ymid, Yend):
        self.possible = True
        for objet in self.objets:
            if objet.name == Name:
                print('existe deja')
                self.possible = False
        if self.possible:
            self.objets.append(StartLogo(Name, Ystart, Ymid, Yend))

    def CreateText(self, Name, Xpos, Ypos, Texte):
        self.possible = True
        for objet in self.objets:
            if objet.name == Name:
                print('existe deja')
                self.possible = False
        if self.possible:
            self.objets.append(Text(Name, Xpos, Ypos, Texte, self.font))

    def Delete(self, Name):
        for objet in self.objets: 
            if objet.name == Name:
                objet.Delete()
                self.objets.remove(objet)

    def ShutDown(self):
        self.thrd.Run = False
        pygame.quit()

    def CreateFace(self, Name):
        self.possible = True
        for objet in self.objets:
            if objet.name == Name:
                print('existe deja')
                self.possible = False
        if self.possible:
            self.objets.append(Face(Name))

    def CreateYTtitle(self, Name, title):
        self.possible = True
        for objet in self.objets:
            if objet.name == Name:
                print('existe deja')
                self.possible = False
        if self.possible:
            self.objets.append(YTtext(Name, title))

    def CreateYTpicture(self, Name):
        self.possible = True
        for objet in self.objets:
            if objet.name == Name:
                print('existe deja')
                self.possible = False
        if self.possible:
            self.objets.append(YTpicture(Name))

    def CreateListenRect(self, Name):
        self.possible = True
        for objet in self.objets:
            if objet.name == Name:
                print('existe deja')
                self.possible = False
        if self.possible:
            self.objets.append(ListenRect(Name))

    def GetObject(self, Name):
        self.objet = False
        for objet in self.objets:
            if objet.name == Name:
                return objet
        return False
