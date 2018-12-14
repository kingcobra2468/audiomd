import threading
import random
import Queue
import vlc
import os
import sys
import re
import time

inputs = Queue.Queue(10)
tLock = threading.Lock()

class commands(threading.Thread):
    __mp3s = list()
    def __init__(self, userInput): #initializes commands and vlc
        threading.Thread.__init__(self)
        self.userInput = userInput
        self.__readFiles()
        self.__sessionAttributes = {
            'random' : False,
            'pause' : lambda : self.player.pause(),
            'play' : lambda : self.player.pause(),
            'skip' : self.__getSong,
            'shift' : lambda sec : self.player.set_time(self.player.get_time() + (sec*1000))
        }
        self.instance=vlc.Instance()
        self.player=self.instance.media_player_new()
        self.__playSong(0)

    def __readFiles(self): #pulls all songs from directory
        self.mp3directory = sys.argv[1] if len(sys.argv) > 1 else "/home/{}/Desktop/".format(os.environ["USER"])
        if not os.path.isdir(self.mp3directory):
            print "Specified directory does not exist"
            exit()
        elif (self.mp3directory[-1] is not "\\") and (os.name is 'nt'):
            self.mp3directory+="\\"
        elif self.mp3directory[-1] is not '//' and os.name is 'posix':
            self.mp3directory+="/"
        for (root, directories, files) in os.walk(os.path.abspath(self.mp3directory)):
            self.__mp3s=[file for file in files if re.search(r'.mp3', file)]
             
    def __getSong(self): #pull song
        self.player.stop()
        if len(self.__mp3s) <= 0:
            self.__readFiles()
            print len(self.__mp3s)
        num=random.randint(0, len(self.__mp3s)-1) if self.__sessionAttributes['random'] else 0
        self.__playSong(num)

    def __playSong(self, index): #play song
        self.media = self.instance.media_new("{0}{1}".format(self.mp3directory, self.__mp3s[index]))
        self.__mp3s.pop(index)
        self.player.set_media(self.media)
        self.player.play()
    def run(self):
        while self.userInput.isAlive():
            self.getAction()
            if self.player.get_state() == vlc.State.Ended:
                self.__getSong()
            time.sleep(1)

    def getAction(self): #get user input
        while not inputs.empty():
            input = inputs.get()
            inputAttr = [atrribute for atrribute in self.__sessionAttributes.keys() if re.search(r"{}".format(atrribute), input, re.IGNORECASE)]
            if len(input.split()) == 1 and len(inputAttr):
                self.__sessionAttributes[inputAttr[0]]()
            elif len(input.split()) == 2 and len(inputAttr):
                if type(self.__sessionAttributes[inputAttr[0]]) is type(bool()):
                    self.__sessionAttributes[inputAttr[0]] = input.split()[-1]  
                else:
                    self.__sessionAttributes[inputAttr[0]](int(input.split()[-1]))
            else:
                print "Invalid Input"
            time.sleep(1)  

class userInput(threading.Thread):
    def getInputInput(self):
        while True:
            input=raw_input(">> : ")
            if re.search(r'[Qq]uit+', input, re.IGNORECASE):
                break
            else:
                inputs.put(input)
                time.sleep(1)
    def run(self):
        tLock.acquire()
        self.getInputInput()
        tLock.release()
   
try:
    userInputThread = userInput()
    commandsThread = commands(userInputThread)
    userInputThread.setDaemon(True)
    userInputThread.start()
    commandsThread.start()
    userInputThread.join()
    commandsThread.join()
except KeyboardInterrupt:
    userInputThread.join()
    commandsThread.join()


#class threading:
#    def readFiles():
#        for (root, directories, files) in os.walk(os.path.abspath("/home/{}/Desktop".format(os.environ["USER"]))):
#            mp3s=[file for file in files if re.search(r'.mp3', file)] 

#one thread taking input from commant line
#other thread playing the mp3s