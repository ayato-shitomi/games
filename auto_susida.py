# Windows環境で実行
# インストールの必要がある
#   C:\\Program Files\\Tesseract-OCR\\tesseract.exe

import pyautogui
import keyboard
import time
from PIL import ImageGrab
import cv2
from PIL import Image
import pyocr
import pyocr.builders
import random

class Point:
    x = 0
    y = 0

def get_mouse_position():
    while True:
        if keyboard.read_key() == "c":
            pos = pyautogui.position()
            return pos

def init():
    print("init")
    # 始点 PyautoGUIによりマウス座標の取得
    begin = get_mouse_position()
    print("begin:","\t",begin)
    time.sleep(1)
    # 終点 PyautoGUIによりマウス座標の取得
    end = get_mouse_position()
    print("end:","\t",end)
    return begin, end

def start(begin, end):
    x, y = (begin.x + end.x) // 2, (begin.y + end.y) // 2
    pyautogui.moveTo(x, y)
    pyautogui.click()
    pyautogui.press('enter')
    
def calculate_point(w_begin, w_end):
    begin, end = Point(), Point()
    begin.x, begin.y = w_begin.x, w_begin.y + (w_end.y - w_begin.y) // 3 * 1
    end.x, end.y = w_end.x, w_begin.y + (w_end.y - w_begin.y) // 3 * 2
    return begin, end
    
def get_str(begin, end, engine):
    img = ImageGrab.grab(bbox=(begin.x + 180, begin.y + 90, end.x - 180, end.y - 20))
    #img.convert('L').show()
    return engine.image_to_string(img, lang="eng")

if __name__ == '__main__':
    pyocr.tesseract.TESSERACT_CMD = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
    pyocr.tesseract.CUNEIFORM_CMD = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
    engines = pyocr.get_available_tools()
    engine = engines[0]
    begin, end = init()
    start(begin, end)
    time.sleep(2)
    str_b, str_e = calculate_point(begin, end)
    while True:
        text = get_str(str_b, str_e, engine)
        pyautogui.write(text, interval=random.uniform(0.1, 0.25))
        #pyautogui.write(text, interval=0.3)
        #pyautogui.write(text)
        #time.sleep(0.5)
