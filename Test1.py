import sounddevice as sd #mic input
import numpy as np #converting mic input data into number
import psutil #going to use this to scan task manager and kill fortnite
import matplotlib.pyplot as plt #image display
import matplotlib.image as mpimg #image display

process_name = "Fortnite"

duration = True



def checkIfProcessRunning(processName): ##checks to see if Task Manager is running Fortnite, then kills it and displays a fat Take the L to my brother
        for proc in psutil.process_iter():
            try:
               if processName.lower() in proc.name().lower():
                    proc.kill()
                    img = mpimg.imread("TaketheL!2.png")
                    plt.imshow(img)
                    plt.show()
            except(psutil.NoSuchProcess, psutil.AccessDenied. psutil.ZombieProcess):
                    pass
        return False;


def print_sound(indata, outdata, frames, time, status): ##this is the callback function which is responsible for getting audio input and output
    volume_norm=np.linalg.norm(indata)*10 ##numpy magic that I grabbed off of https://github.com/arupiot/Sound-level-meter/blob/master/slm.py
    if (volume_norm > 420.69):
        checkIfProcessRunning(process_name)
        duration = False


while duration:
    with sd.Stream(callback=print_sound): #opens up an audio stream that collects mic input
        sd.sleep(1000)
