import win32api,win32con
import time

recoil_y_value = 5
recoil_x_value = 0

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
    global recoil_y_value
    recoil_y_value-=1

def lower_recoil():
    global recoil_y_value
    recoil_y_value+=1


def decrease_left_recoil():
    global recoil_x_value
    recoil_x_value+=1
 
def decrease_right_recoil():
    global recoil_x_value
    recoil_x_value-=1
 
def modify_recoil():
    numpad_10 = win32api.GetKeyState(0x68)
    numpad_2 = win32api.GetKeyState(0x62)
    numpad_4 = win32api.GetKeyState(0x64)
    numpad_6 = win32api.GetKeyState(0x66)
    if(numpad_10 < -1):
        increase_recoil()
        time.sleep(0.15)
    
    elif(numpad_2 < -1):
        lower_recoil()
        time.sleep(0.15)
    
    elif(numpad_4 < -1):
        decrease_right_recoil()
        time.sleep(0.15)
    
    elif(numpad_6 < -1):
        decrease_left_recoil()
        time.sleep(0.15)
    else:
        return False
    

print("App started")
while(interrupt() == False):
    if(modify_recoil() != False):
        print("Current recoil....  y : " + str(recoil_y_value) + " x : " + str(recoil_x_value))
    if(is_mouse_down()):
        for x in range(0, 55):
            # start = time.time()
            time.sleep(0.016)
            if(is_mouse_down()):
                
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, int(recoil_x_value), int(recoil_y_value), 0, 0)
                # print(f'Time: {time.time() - start}')
            else:
                break
        for x in range(0, 20):
            time.sleep(0.016)
            if(is_mouse_down()):
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, int(recoil_x_value), int(recoil_y_value), 0, 0)
            else:
                break
    time.sleep(0.002)

