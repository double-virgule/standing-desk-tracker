#!/usr/bin/env python3
import tkinter as Tkinter 
from datetime import datetime 
import time
import csv

Standing_Run = False
Sitting_Run = False
FullStanding_Time = 0
FullSitting_Time = 0
StandingStart_Time = 0
SittingStart_Time = 0
StandingEnd_Time = 0 
SittingEnd_Time = 0

def Sitting(label):
    global Standing_Run
    global Sitting_Run
    global FullStanding_Time
    global FullSitting_Time
    global StandingStart_Time
    global SittingStart_Time
    global StandingEnd_Time
    global SittingEnd_Time

    print(Sitting_Run)
    print(Standing_Run)

    if (Standing_Run == True):
        Standing_Run = False
        StandingEnd_Time = time.time()
        TemporaryMath = StandingEnd_Time - StandingStart_Time
        FullStanding_Time = TemporaryMath + FullStanding_Time
    Sitting_Run = True
    SittingStart_Time = time.time()
    CurrentTimePretty = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    label['text']=CurrentTimePretty
    sitting['state']='disabled'
    standing['state']='normal'

def Standing(label):
    global Standing_Run
    global Sitting_Run
    global FullStanding_Time
    global FullSitting_Time
    global StandingStart_Time
    global SittingStart_Time
    global StandingEnd_Time
    global SittingEnd_Time

    print(Sitting_Run)
    print(Standing_Run)

    if (Sitting_Run == True):
        Sitting_Run = False
        SittingEnd_Time = time.time()
        TemporaryMath = SittingEnd_Time - SittingStart_Time
        FullSitting_Time = TemporaryMath + FullSitting_Time
        print(FullSitting_Time)
    Standing_Run = True
    StandingStart_Time = time.time()
    CurrentTimePretty = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    label['text']=CurrentTimePretty
    standing['state']='disabled'
    sitting['state']='normal'

def ExitProgram():

    print(FullSitting_Time)
    print(FullStanding_Time)

    sample_mod=[['SittingTime', FullSitting_Time, 'StandingTime', FullStanding_Time]]
    with open('standingsittingtime.txt', 'w') as f:
        w = csv.writer(f, dialect = 'excel-tab')
        w.writerows(sample_mod)
    root.destroy()
    exit


root = Tkinter.Tk() 
root.title("Standing/Sitting Tracker") 
root.minsize(width=250, height=70) 
label = Tkinter.Label(root, text="Welcome!", fg="black", font="Verdana 10 bold") 
label.pack() 
f = Tkinter.Frame(root) 
standing = Tkinter.Button(f, text='Standing', width=6, command=lambda:Standing(label)) 
sitting = Tkinter.Button(f, text='Sitting',width=6, command=lambda:Sitting(label)) 
exitbutton = Tkinter.Button(f, text='Exit',width=6, command=ExitProgram) 
f.pack(anchor = 'center',pady=5) 
standing.pack(side="left") 
sitting.pack(side ="left") 
exitbutton.pack(side="left") 
root.mainloop() 

#####










