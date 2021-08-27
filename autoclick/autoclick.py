# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 21:35:28 2021

@author: alile
"""


import keyboard
import time
import pyautogui

marche= True
while True:
    keyboard.wait('*')
    marche=True
    while(marche):
        pyautogui.click()
        time.sleep(0.5)
        if keyboard.is_pressed('-'):
            marche=False
        