import mss
import mss.tools


def capture_screen():
    with mss.MSS() as sct:
        monitor = sct.monitors[1]
        screenshot = sct.grab(monitor)
        photo = mss.tools.to_png(screenshot.rgb, screenshot.size)
        return photo