# -*- coding: utf-8 -*-
"""
Created on Mon May 23 15:08:49 20bbb20

@author: HuangRen
"""

import os
import keyboard  # using module keyboard

while True:  # making a loop
    keyboard.read_key()
    if keyboard.is_pressed('esc'):  # if key 'q' is pressed
        print('done!')
        break  # finishing the loop
    if keyboard.is_pressed('page down'):  # if key 'q' is pressed
        print('[PAGE DOWN]')
    if keyboard.is_pressed('page up'):  # if key 'q' is pressed
        print('[PAGE UP]')
    if keyboard.is_pressed('left'):  # if key 'q' is pressed
        print('[RIGHT]')
    if keyboard.is_pressed('right'):  # if key 'q' is pressed
        print('[LEFT]')
    if keyboard.is_pressed('up'):  # if key 'q' is pressed
        print('[UP]')
    if keyboard.is_pressed('down'):  # if key 'q' is pressed
        print('[DOWN]')
