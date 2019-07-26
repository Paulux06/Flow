from threading import Thread
from Modules.Snowboy import snowboydecoder
import signal

class AudioDetection(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.Detected = False
        signal.signal(signal.SIGINT, self.signal_handler)
        self.detector = snowboydecoder.HotwordDetector('./Modules/Snowboy/Flow.pmdl', sensitivity=0.45)
        self.interrupted = False
        self.CommandFound = 'False'

    def run(self):
        self.detector.start(detected_callback=self.SetCommand,
                        interrupt_check=self.interrupt_callback,
                        sleep_time=0.03)

    def signal_handler(self, signal, frame):
        self.interrupted = True

    def interrupt_callback(self):
        return self.interrupted

    def SetCommand(self):
        if self.CommandFound == 'False':
            self.CommandFound = 'True'

    def Shutdown(self):
        self.detector.terminate()