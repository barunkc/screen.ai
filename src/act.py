import pyautogui

def move_mouse(x, y):
    pyautogui.moveTo(x, y, duration=1)

def click():
    pyautogui.click()

def type_text(text):
    pyautogui.write(text)

def press_key(key):
    pyautogui.press(key)

def hotkey(*keys):
    pyautogui.hotkey(*keys)
click()
hotkey("ctrl", "a")
