import pygame
import datetime
import time

t1 = 18
t2 = 30
t3 = 45
while (True):
    t = datetime.datetime.now()
    if int(t.hour) == 17:
        break

    def playSound():
        pygame.mixer.init()
        pygame.mixer.music.load(song) 
        pygame.mixer.music.set_volume(1) 
        pygame.mixer.music.play(-1)
        stop = input("Enter DONE to stop: ")
        if stop.lower() == "done":
            pygame.mixer.music.stop()
            f = open("log.txt", "a")
            f.write(f"[{datetime.datetime.now()}]  {add}\n")
            f.close
            print("mentioned in the log")
        else:
            print("wrong input")
            playSound()

    if t1 == 0 and t2 == 0 and t3 == 0:
        song = "waterPhyExerEyeExer.mp3"
        add = "drank water , eye exercise and physical exercise done"
        playSound()
        t1,t2,t3 = 18,30,45

    elif t1 == 0 and t2 == 0:
        song = "waterEyeExer.mp3"
        add = "drank water and eye exercise done"
        playSound()
        t1,t2 = 18,30

    elif t3 == 0 and t1 == 0:
        song = "waterPhyExer.mp3"
        add = "drank water and physical exercise done"
        playSound()
        t3,t1 = 45,18

    elif t3 == 0 and t2 == 0:
        song = "eyeAndPhy.mp3"
        add = "Eye exercise and physical exercise"
        playSound()
        t3,t2 = 45,30

    elif t1 == 0:
        song = "water.mp3"
        add = "drank water"
        playSound()
        t1 = 18

    elif t2 == 0:
        song = "eye.mp3"
        add = "Eye exercise done"
        playSound()
        t2 = 30

    elif t3 == 0:
        song = "phyExer.mp3"
        add = "Physical exercise done"
        playSound()
        t3 = 45

    time.sleep(60)
    t1 -= 1
    t2 -= 1
    t3 -= 1
    
