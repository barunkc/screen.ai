import keyboard
from main import process_screen


def activate():
    print("screen.ai activated!")
    process_screen()


keyboard.add_hotkey("alt+[", activate)

print("Waiting for Alt + [ ...")
keyboard.wait()