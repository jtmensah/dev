import random
import time
from tkinter import *

import pyautogui


class Timer():
   def __init__(self):
      self.root = tk.Tk()
      self.label = tk.Label(text="", font=('Times New Roman', 40))
      self.label.pack()
      self.updateClock()
      self.root.mainloop()

   def updateClock(self):
      now = time.strftime("%H:%M:%S")
      self.label.configure(text=now)
      self.root.after(1000, self.updateClock)

running = True

def mouse_movement():
    if running:
        x = random.randint(0,500)
        y = random.randint(0,500)
        pyautogui.moveTo(x,y)
        time.sleep(1)
    window.after(5000, mouse_movement)

def start_mouse():
    global running
    running = True

def stop_mouse():
    global running
    running = False

window = Tk()
window.geometry("250x150")

frame1 = Frame(window)
frame1.pack()

frame2 = Frame(window)
frame2.pack(side=BOTTOM)

start_button = Button(frame1, text="Start Mouse", command=start_mouse, font=("Comic Sans",20), bg="green")
start_button.pack()

stop_button = Button(frame1, text="Stop Mouse", command=stop_mouse, font=("Comic Sans",20), bg="red")
stop_button.pack()

label = Label(frame2, text="Wavey Inc.", font=("Times New Roman",10))
label.pack(side=BOTTOM)


window.after(5000, mouse_movement)
window.mainloop()