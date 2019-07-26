import pygame, math

class Loading:
    def __init__(self, Name, Xmin, Ymin, Xmax, Ymax):
        self.Xmax = Xmax
        self.Xmin = Xmin
        self.Ymax = Ymax
        self.Ymin = Ymin
        self.name = Name
        self.progress = Xmin
        self.Xsize = 0
        self.deleted = False
        self.delete = False

    def Refresh(self, Screen):
        if self.delete == False:
            if self.progress > self.Xmax:
                self.progress = self.Xmin

            self.Xsize = (1-math.sqrt(((self.progress-self.Xmin)-((self.Xmax-self.Xmin)/2))**2) /((self.Xmax-self.Xmin)/2))*120
        self.progress += self.Xsize/30+4
        pygame.draw.rect(Screen, (self.Xsize*2, self.Xsize*2, self.Xsize*2), (self.progress-self.Xsize/2, self.Ymin, self.Xsize, self.Ymax-self.Ymin))

    def Delete(self):
        self.delete = True
        for i in range(int(self.Xsize),0,-1):
            self.Xsize = i
            pygame.time.wait(1)
        self.Deleted = True


class StartLogo:
    def __init__(self, Name, YStart, Ymid, Yend):
        self.Xpos = 515
        self.YStart = YStart
        self.Ymid = Ymid
        self.Yend = Yend
        self.name = Name
        self.Ypos = YStart
        self.step = 0
        self.deleted = False
        self.delete = False
        self.image = pygame.transform.scale(pygame.image.load('./Ressources/Flow_Logo.png').convert(), (250,250))
        self.image.set_alpha(255)

    def Refresh(self, Screen):
        if self.step == 0:
            Screen.blit(self.image, (self.Xpos, self.Ypos))
            self.Ypos += (self.Ymid-self.Ypos)/20-2
            if self.Ypos < self.Ymid:
                self.step = 1

        if self.step == 1:
            Screen.blit(self.image, (self.Xpos, self.Ypos))
            self.Ypos += (self.Yend-self.Ypos)/20+2
            if self.Ypos > self.Yend:
                self.step = 2

        if self.step == 2:
            Screen.blit(self.image, (self.Xpos, self.Ypos))

    def Delete(self):
        self.delete = True
        for i in range(255, 0, -1):
            self.image.set_alpha(i)
            pygame.time.wait(1)
        self.Deleted = True

class Text:
    def __init__(self, Name, Xpos, Ypos, Texte, Font):
        self.name = Name
        self.delete = False
        self.Deleted = False
        self.font = Font
        self.text = Texte
        self.color = (255,255,255)
        self.Xpos = Xpos
        self.Ypos = Ypos

    def Refresh(self, Screen):
        Screen.blit(self.font.render(self.text, True, self.color), (self.Xpos, self.Ypos))

    def Delete(self):
        self.delete = True
        for i in range(255, 0, -5):
            self.color = i,i,i
            pygame.time.wait(1)
        self.Deleted = True

class Face:
    def __init__(self, Name):
        self.name = Name
        from Modules.FaceReco import FaceReco
        self.Reco = FaceReco()
        self.normal_face = pygame.transform.scale(pygame.image.load('./Ressources/normal_face.png').convert(), [1280,720])
        self.weary_face = pygame.transform.scale(pygame.image.load('./Ressources/weary_face.png').convert(), [1280,720])
        self.happy_face = pygame.transform.scale(pygame.image.load('./Ressources/happy_face.png').convert(), [1280,720])
        self.shocked_face = pygame.transform.scale(pygame.image.load('./Ressources/shocked_face.png').convert(), [1280,720])
        self.sick_face = pygame.transform.scale(pygame.image.load('./Ressources/sick_face.png').convert(), [1280,720])
        self.sleeping_face = pygame.transform.scale(pygame.image.load('./Ressources/sleeping_face.png').convert(), [1280,720])
        self.image = self.normal_face
        self.Xpos = 0
        self.Ypos = 0
        self.delete = False
        self.Deleted = False
        self.image_name = ''
        self.show = True

    def SetFace(self, name):
        if self.image_name == name:
            return True
        for i in range(255,0,-10):
            self.image.set_alpha(i)
            pygame.time.wait(1)
        if name == 'normal':
            self.image = self.normal_face
        if name == 'weary':
            self.image = self.weary_face
        if name == 'happy':
            self.image = self.happy_face
        if name == 'shocked':
            self.image = self.shocked_face
        if name == 'sick':
            self.image = self.sick_face
        if name == 'sleeping':
            self.image = self.sleeping_face
        self.image_name = name
        for i in range(0,255,10):
            self.image.set_alpha(i)
            pygame.time.wait(1)

    def Hide(self):
        self.show = False
        for i in range(255,0,-5):
            self.image.set_alpha(i)
            pygame.time.wait(1)
        self.image.set_alpha(0)

    def Show(self):
        self.show = True
        for i in range(0,255,5):
            self.image.set_alpha(i)
            pygame.time.wait(1)
        self.image.set_alpha(255)
        
    def IsPerson(self):
        return self.Reco.GetPerson()

    def Pause(self):
        self.Reco.Pause()

    def Play(self):
        self.Reco.Play()

    def Refresh(self, Screen):
        self.Xpos = self.Reco.Get_Xpos()*120
        self.Ypos = self.Reco.Get_Ypos()*90
        Screen.blit(self.image, (self.Xpos, self.Ypos))

    def Delete(self):
        self.delete = True
        self.Reco.Shutdown()
        if self.show:
            for i in range(255,0,-1):
                self.image.set_alpha(i)
                pygame.time.wait(1)
        self.Deleted = True


class YTpicture:
    def __init__(self, Name):
        self.image = pygame.transform.scale(pygame.image.load("./Ressources/Minia.jpg").convert(), [320,180])
        self.background = pygame.transform.scale(pygame.image.load("./Ressources/Minia.jpg").convert(), [1280,720])
        self.background.set_alpha(20)
        self.name = Name
        self.delete = False
        self.Deleted = False
        self.Xpos = 480
        self.Ypos = 120
        self.alpha = 255

    def Refresh(self, Screen):
        Screen.blit(self.background, (0, 0))
        Screen.blit(self.image, (self.Xpos, self.Ypos))

    def Delete(self):
        self.delete = True
        for self.alpha in range(255, 0, -2):
            self.image.set_alpha(self.alpha)
            pygame.time.wait(1)
        self.Deleted = True
        
class YTtext:
    def __init__(self, Name, Text):
        self.font = pygame.font.SysFont('arial', 32)
        self.name = Name
        self.delete = False
        self.Deleted = False
        self.text = Text
        self.alpha = 0
        try:
            self.textrendered = self.font.render(self.text, True, [0,0,0])
        except:
            self.text = "Titre inconnu"
            self.textrendered = self.font.render(self.text, True, [0,0,0])
        self.Ysize = self.font.size(self.text)[1]
        self.Xsize = self.font.size(self.text)[0]
        self.Xpos = 640-(self.Xsize/2)
        self.Ypos = 540-(self.Ysize/2)

    def Refresh(self, Screen):
        if self.alpha < 255:
            self.alpha += 5
            self.textrendered = self.font.render(self.text, True, [self.alpha, self.alpha, self.alpha])
        Screen.blit(self.textrendered, (self.Xpos, self.Ypos))

    def Delete(self):
        self.delete = True
        for self.alpha in range(255, 0, -5):
            self.textrendered = self.font.render(self.text, True, [self.alpha, self.alpha, self.alpha])
            pygame.time.wait(1)
        self.Deleted = True

class ListenRect:
    def __init__(self, Name):
        self.name = Name
        self.delete = False
        self.Deleted = False
        self.color = 0

    def Refresh(self, Screen):
        if self.delete == False and self.color != 255:
            self.color += 5
        pygame.draw.rect(Screen, (self.color, self.color, self.color), (0,0,1280,720), int(round(self.color/51+1, 0)))

    def Delete(self):
        self.delete = True
        for i in range(255, 0, -5):
            self.color = i
            pygame.time.wait(1)
        self.Deleted = True
