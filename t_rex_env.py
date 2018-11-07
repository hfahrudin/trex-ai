import numpy as np
import cv2
from PIL import ImageGrab
import time
import pyautogui
import matplotlib.pyplot as plt
from ai import Dqn
#
last_time = time.time()
def process_img(original_image):
    processed_img = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    processed_img = cv2.resize(processed_img,(80,80))
    return processed_img

def saveall(ai, data):
    ai.save()
    plt.plot(data)
    plt.savefig('progression.png')
    
last_reward = 0
memo = []
brain = Dqn((1,80,80),3,0.9)
condition = True
last_state = np.zeros((1,80,80))
counter = 0
steps_count = 0
mean_steps = 0
scores = []
up_pressed = False
dino = cv2.cvtColor(cv2.imread('game_over.png'), cv2.COLOR_BGR2GRAY)
w, h = dino.shape[:2]
brain.load()
while(condition):
    
    action = brain.update(last_reward, last_state)
    
    if action == 2 :
        pyautogui.keyUp('down')
        pyautogui.keyDown('up')
    elif action == 0:
        pyautogui.keyUp('up')
        pyautogui.keyUp('down')
    else:
        pyautogui.keyUp('up')
        pyautogui.keyDown('down')
#        
    screen = np.array(ImageGrab.grab(bbox=(5,155,600,296)))
    a = process_img(screen)
    proc_img = np.expand_dims(a, axis=0) 

    processed_img = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
    match = cv2.matchTemplate(processed_img, dino ,cv2.TM_CCOEFF_NORMED)
    threshold = 0.9
    loc = np.where( match >= threshold)
    if loc[0].size > 0:
       last_reward = -85
       if counter == 20:
           counter = 0
           scores.append(mean_steps/20)
           mean_steps = 0
           saveall(brain, scores)
       else:
           counter +=1
           mean_steps+=steps_count
       time.sleep(1)
       pyautogui.press('up')
       steps_count = 0
    else:
        last_reward = steps_count
    if len(scores) > 50 :
        break
    steps_count +=1 
    last_state = proc_img
    
