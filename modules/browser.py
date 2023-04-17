import time
import webbrowser
import pyautogui

def open_browser(url):
    browser = webbrowser.get('firefox')
    browser.open_new(url)
    time.sleep(10)

def type_message(message):
    pyautogui.write(message)
    pyautogui.press('enter')
    time.sleep(1)

def close_browser():
    pyautogui.hotkey('ctrl', 'w')
    time.sleep(1)
