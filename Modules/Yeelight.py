from yeelight import discover_bulbs, Bulb

class Lampe:
    def __init__(self):
        self.Offline = False
        try:
            self.Find_Light()
        except OSError:
            self.Offline = True

    def Find_Light(self):
        try:
            self.Adresse = discover_bulbs()[0]['ip']
            self.light = Bulb(self.Adresse)
        except IndexError:
            print('Aucune ampoule Yeelight trouvée')

    def Turn_On(self):
        self.light.turn_on()

    def Turn_Off(self):
        self.light.turn_off()

    def Color_Blue(self):
        self.light.set_rgb(0, 0, 255)

    def Color_Green(self):
        self.light.set_rgb(0, 255, 0)

    def Color_Red(self):
        self.light.set_rgb(255, 0, 0)

    def Color_White(self):
        self.light.set_rgb(255, 255, 255)
        self.light.set_color_temp(5000)

    def Color_Cold(self):
        self.light.set_color_temp(6000)

    def Color_Hot(self):
        self.light.set_color_temp(3500)

    def Reset_Light(self):
        self.light.set_rgb(255, 255, 255)
        self.light.set_brightness(100)
        self.light.set_color_temp(5500)

    def Bright_Max(self):
        self.light.set_brightness(100)

    def Bright_Min(self):
        self.light.set_brightness(0)

    def Bright(self, value):
        self.light.set_brightness(value)
