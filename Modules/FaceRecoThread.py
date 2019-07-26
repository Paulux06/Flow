from threading import Thread
import numpy as np
import cv2, requests

class FaceRecog(Thread):
    def __init__(self):
        Thread.__init__(self)
        try:
            self.source = requests.get('http://192.168.43.1:8080/video', stream=True)
        except:
            self.source = 'Unknown'
        self.xmlfile = cv2.CascadeClassifier('./Modules/face.xml')
        self.results = []
        self.Xaxis = 0
        self.Yaxis = 0
        self.OldX = 0
        self.OldY = 0
        self.Face = False
        self.bytes = bytes()
        self.free = False
        self.Run = True
        self.Ready = False

    def run(self):
        if self.source != 'Unknown':
            for chunk in self.source.iter_content(chunk_size=512):
                if self.Run == False:
                    break
                self.bytes += chunk
                self.a = self.bytes.find(b'\xff\xd8')
                self.b = self.bytes.find(b'\xff\xd9')
                if self.a != -1 and self.b != -1:
                    self.jpg = self.bytes[self.a:self.b+2]
                    self.bytes = self.bytes[self.b+2:]
                    try:
                        self.i = cv2.imdecode(np.fromstring(self.jpg, dtype=np.uint8), cv2.IMREAD_COLOR)
                    except:
                        print('Error: Buffer empty')
                    self.gray = cv2.cvtColor(self.i, cv2.COLOR_BGR2GRAY)
                    self.faces = self.xmlfile.detectMultiScale(self.gray, 1.3, 5)
                    if self.Face != 'Wait':
                        self.Face = False
                    self.OldX = self.Xaxis
                    self.OldY = self.Yaxis
                    for (x,y,w,h) in self.faces:
                        if self.Face == False:
                            self.Face = True
                            self.Xaxis = (x+x+w)/2
                            self.Yaxis = (y+y+h)/2
                    if self.Face == True:
                        self.Xaxis = int(round(self.OldX+(self.Xaxis-self.OldX)/5, 0))
                        self.Yaxis = int(round(self.OldY+(self.Yaxis-self.OldY)/5, 0))
                    else:
                        self.Xaxis = int(round(self.Xaxis-(self.Xaxis-320)/10, 0))
                        self.Yaxis = int(round(self.Yaxis-(self.Yaxis-220)/10, 0))
                self.results = self.Xaxis-320, self.Yaxis-240
                self.free = True
            self.Ready = True

        else:
            return 'Unknown'
