from tkinter import *
import pyautogui
import time
import win32api
import win32con

running = False

'''' 
libraries to install in cmd
pip install pyautogui
pip install pywin32
pip install pillow(may ask to install)
'''


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def img(img_name):
    if pyautogui.locateOnScreen(img_name) is not None:
        x, y = pyautogui.locateCenterOnScreen(img_name)
        click(x, y)
        time.sleep(1)
    else:
        time.sleep(1)


def call(img_name):
    try:
        img(img_name)
        time.sleep(1)
    except:
        time.sleep(1)


def scanning():
    if running:
        call('a.png')  # save the image you want to click in the ms-paint and save it as a.png in the file directory
        call('b.png')  # save the image you want to click in the ms-paint and save it as b.png in the file directory
        call('c.png')  # save the image you want to click in the ms-paint and save it as c.png in the file directory
        call('d.png')  # save the image you want to click in the ms-paint and save it as d.png in the file directory

    root.after(1000, scanning)


def start():
    start.config(state=DISABLED)
    start["bg"] = "black"
    stop["bg"] = "white"
    stop.config(state=NORMAL)
    global running
    running = True


def stop():
    stop.config(state=DISABLED)
    stop["bg"] = "black"
    start["bg"] = "white"
    start.config(state=NORMAL)
    global running
    running = False


root = Tk()
root.title("Title")
root.geometry("200x70")

app = Frame(root)
app.grid()

start = Button(app, text="Start", command=start, state=NORMAL, padx=79)
stop = Button(app, text="Stop ", command=stop, state=DISABLED, padx=77, bg='black')


start.grid()
stop.grid()

root.after(1000, scanning)
root.mainloop()
