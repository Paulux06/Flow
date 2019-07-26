import pygame
from threading import Thread

class Refresher(Thread):
    def __init__(self, screen, objets):
        Thread.__init__(self)
        self.screen = screen 
        self.objets = objets
        self.Run = True
        self.Ready = False

    def run(self):
        while self.Run:
            self.screen.fill((0,0,0))
            for objet in self.objets:
                objet.Refresh(self.screen)
            pygame.display.flip()
            pygame.time.wait(5)
        self.Ready = True