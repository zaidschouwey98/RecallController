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


def control():
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, int(0), int(4), 0, 0)


def is_mouse_down():    # Returns true if the left mouse button is pressed
    lmb_state = win32api.GetKeyState(0x01)
    rmb_state = win32api.GetKeyState(0x02)
    if(lmb_state < -1 and rmb_state < -1):
        return True
    else:
        return False



while(1):
    if(is_mouse_down()):
        for x in range(0, 55): # 55
            # start = time.time()
            time.sleep(0.016)
            if(is_mouse_down()):
                
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, int(0), int(9), 0, 0)
                # print(f'Time: {time.time() - start}')
            else:
                break
        for x in range(0, 20):
            time.sleep(0.015)
            if(is_mouse_down()):
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, int(0), int(9), 0, 0)
            else:
                break
# mouse.on_button(control ,args=(), buttons=('left'), types=('down'))
    # mouse.wait(button='right', target_types=( 'down'))
    # while(mouse.is_pressed(button='right') and mouse.is_pressed(button="left")):
    #     win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, int(0), int(1), 0, 0)
        # print("test")
        # pos = mouse.get_position()
        # mouse.move(pos[0], pos[1]+4, absolute=True, duration=0)

    time.sleep(0.002)

