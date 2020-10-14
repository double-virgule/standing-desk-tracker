import tkinter as Tkinter 
from datetime import datetime 
import time
import csv 

global Sitting_Run
global Standing_Run
global FullStanding_Time
global FullSitting_Time
global StandingStart_Time
global SittingStart_Time
global StandingEnd_Time
global SittingEnd_Time

def Sitting(label):  
    if (Standing_Run == True):
        Standing_Run = False
        StandingEnd_Time = time.time()
        TemporaryMath = StandingEnd_Time - StandingStart_Time
        FullStanding_Time = TemporaryMath + FullStanding_Time
    Sitting_Run == True
    SittingStart_Time = time.time()
    CurrentTimePretty = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(1347517370))
    label['text']=CurrentTimePretty
    Sitting['state'] = 'Disabled'
    Standing['state'] = 'Normal'

def Standing(label):
    if (Sitting_Run == True):
        Sitting_Run = False
        SittingEnd_Time = time.time()
        TemporaryMath = SittingEnd_Time - SittingStart_Time
        FullSitting_Time = TemporaryMath + FullSitting_Time
    Sitting_Run == True
    SittingStart_Time = time.time()
    CurrentTimePretty = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(1347517370))
    label['text']=CurrentTimePretty
    Standing['state'] = 'Disabled'
    Sitting['state'] = 'Normal'

def ExitProgram():
    #Write to CSV 
	
	#[Standing Time]    [Sitting Time]
	#[FullStanding_Time][FullSitting_Time]
    root.destroy()
    exit


root = Tkinter.Tk() 
root.title("Standing/Sitting Tracker") 
root.minsize(width=250, height=70) 
label = Tkinter.Label(root, text="Welcome!", fg="black", font="Verdana 30 bold") 
label.pack() 
f = Tkinter.Frame(root) 
start = Tkinter.Button(f, text='Standing', width=6, command=lambda:Standing(label)) 
stop = Tkinter.Button(f, text='Sitting',width=6, command=lambda:Sitting(label)) 
exitbutton = Tkinter.Button(f, text='Exit',width=6, command=ExitProgram) 
f.pack(anchor = 'center',pady=5) 
start.pack(side="left") 
stop.pack(side ="left") 
exitbutton.pack(side="left") 
root.mainloop() 

#####










