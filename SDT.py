import time
from tkinter import *

def time_convert(sec):
      mins = sec // 60
      sec = sec % 60
      hours = mins // 60
      mins = mins % 60
      print("Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),sec))

def Standing():
    print("Standing")

def Sitting():
    print("Sitting")

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)        
        self.master = master

        # widget can take all window
        self.pack(fill=BOTH, expand=1)
        
        sitButton = Button(self, text="Sitting", command= Sitting)

        standButton = Button(self, text="Standing", command= Standing)
        
        exitButton = Button(self, text="Exit", command= self.clickExitButton)
        
        #sitButton.place(x=0, y=0)
        sitButton.grid(row=0,column=0)
        standButton.grid(row=0,column=1)
        exitButton.grid(row=0,column=2)

    def clickExitButton(self):
        exit()
        
root = Tk()
app = Window(root)
root.wm_title("Tkinter button")
root.geometry("320x200")


root.mainloop()



#input("Press Enter to start")
#start_time = time.time()
#input("Press Enter to stop")
#end_time = time.time()
#time_lapsed = end_time - start_time
#time_convert(time_lapsed)

