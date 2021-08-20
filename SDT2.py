#!/usr/bin/env python3
import tkinter as Tkinter # sudo apt-get install python3-tk 
from datetime import datetime 
import time
import os

### Sets variables

Standing_Run = False
Sitting_Run = False
FullStanding_Time = 0
FullSitting_Time = 0
StandingStart_Time = 0
SittingStart_Time = 0
StandingEnd_Time = 0 
SittingEnd_Time = 0
StandingSittingTotals = ""

###

def time_convert(sec):
    mins = sec // 60
    sec = sec % 60
    hours = mins // 60
    mins = mins % 60
    formatted = "{0}:{1}:{2}".format(int(hours),int(mins),sec)
    return formatted


def Sitting(label):
    print("Sitting")
    global FullStanding_Time, FullSitting_Time, StandingStart_Time, SittingStart_Time, StandingSittingTotals

    current_time = datetime.now().strftime("%H:%M:%S")

    SittingStart_Time = time.time() 
    
    if (FullStanding_Time != 0):
        StandingEnd_Time = time.time()
        TempMath = StandingEnd_Time - StandingStart_Time 
        FullStanding_Time = FullStanding_Time + TempMath

    if (FullStanding_Time == 0): 
        FullStanding_Time = 0.001

    print("FullStanding_Time = " + str(FullStanding_Time))
    print("FullSitting_Time = " + str(FullSitting_Time))

    p_fullstandtime = time_convert(int(FullStanding_Time))
    p_fullsittime = time_convert(int(FullSitting_Time))

    StandingSittingTotals = "Total Sitting Time: " + str(p_fullsittime) + "\nTotal Standing Time: " + str(p_fullstandtime) + "\nStarted Standing at " + str(current_time)
    label['text'] = StandingSittingTotals


    file1 = open("standingsitting.txt", "w") 
    file1.write(StandingSittingTotals)
    file1.close()

    sitting['state']='disabled'
    standing['state']='normal'

def Standing(label):
    print("Standing")
    global FullStanding_Time, FullSitting_Time, StandingStart_Time, SittingStart_Time, StandingSittingTotals

    current_time = datetime.now().strftime("%H:%M:%S")

    StandingStart_Time = time.time() 

    if (FullSitting_Time != 0):
        SittingEnd_Time = time.time()
        TempMath = SittingEnd_Time - SittingStart_Time 
        FullSitting_Time = FullSitting_Time + TempMath


    if (FullSitting_Time == 0): 
        FullSitting_Time = 0.001

    p_fullstandtime = time_convert(int(FullStanding_Time))
    p_fullsittime = time_convert(int(FullSitting_Time))

    StandingSittingTotals = "Total Sitting Time: " + str(p_fullsittime) + "\nTotal Standing Time: " + str(p_fullstandtime) + "\nStarted Sitting at " + str(current_time)

    print("FullStanding_Time = " + str(FullStanding_Time))
    print("FullSitting_Time = " + str(FullSitting_Time))

    label['text'] = StandingSittingTotals 
 
    standing['state']='disabled'
    sitting['state']='normal'

def ExitProgram(FullSitting_Time, FullStanding_Time):
    
    file1 = open("standingsitting.txt", "w") 
    file1.write(StandingSittingTotals)
    file1.close()

    nicedate = datetime.now().strftime("%y_%m_%d")

    os.rename(r'standingsitting.txt',r'standingsitting' + nicedate + ".txt")
    root.destroy()
    exit


root = Tkinter.Tk() 
root.title("Standing/Sitting Tracker") 
root.minsize(width=350, height=75)
label = Tkinter.Label(root, text="Test", font="Verdana 10 bold") 
label.pack() 
f = Tkinter.Frame(root) 
standing = Tkinter.Button(f, text='Standing', width=6, command=lambda:Standing(label)) 
sitting = Tkinter.Button(f, text='Sitting',width=6, command=lambda:Sitting(label)) 
exitbutton = Tkinter.Button(f, text='Exit',width=6, command=lambda:ExitProgram(FullSitting_Time,FullStanding_Time)) 
f.pack(anchor = 'center',pady=5) 
standing.pack(side="left", padx=0,pady=10) 
sitting.pack(side ="left", padx=0,pady=10) 
exitbutton.pack(side="left", padx=0,pady=10) 
root.mainloop() 

#####


