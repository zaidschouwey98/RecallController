import mouse
import keyboard
import time

import win32api,win32con
from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)

while(1):
    print("boucle1")
    mouse.wait(button='right', target_types=( 'down'))
    print("boucle2")
    while(mouse.is_pressed(button='right') and mouse.is_pressed(button="left")):
        print("boucle3")
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, int(0), int(1), 0, 0)
        # print("test")
        # pos = mouse.get_position()
        # mouse.move(pos[0], pos[1]+4, absolute=True, duration=0)





