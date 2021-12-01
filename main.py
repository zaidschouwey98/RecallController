import mouse
import win32api,win32con
from tkinter import *
from tkinter import ttk
import time
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
recoil_x_value = 5
recoil_y_value = 0

def interrupt():
    ctrl_state = win32api.GetKeyState(0x11)
    tkey_state = win32api.GetKeyState(0x54)
    if(ctrl_state < -1 and tkey_state < -1):
        print("Exiting...")
        return True
    else:
        return False

def is_mouse_down():    # Returns true if the left mouse button is pressed
    lmb_state = win32api.GetKeyState(0x01)
    rmb_state = win32api.GetKeyState(0x02)
    if(lmb_state < -1 and rmb_state < -1):
        return True
    else:
        return False
def increase_recoil():
    global recoil_x_value
    recoil_x_value-=1
    print("Current recoil is : " + str(recoil_x_value) )
def lower_recoil():
    global recoil_x_value
    recoil_x_value+=1
    print("Current recoil is : " + str(recoil_x_value))
def modify_recoil():
    numpad_10 = win32api.GetKeyState(0x68)
    if(numpad_10 < -1):
        increase_recoil()
        time.sleep(0.15)
    numpad_2 = win32api.GetKeyState(0x62)
    if(numpad_2 < -1):
        lower_recoil()
        time.sleep(0.15)
    

    

print("App started")
while(interrupt() == False):
    modify_recoil()
    if(is_mouse_down()):
        for x in range(0, 55):
            # start = time.time()
            time.sleep(0.016)
            if(is_mouse_down()):
                
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, int(recoil_y_value), int(recoil_x_value), 0, 0)
                # print(f'Time: {time.time() - start}')
            else:
                break
        for x in range(0, 20):
            time.sleep(0.016)
            if(is_mouse_down()):
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, int(recoil_y_value), int(recoil_x_value), 0, 0)
            else:
                break
    time.sleep(0.002)

