import cv2
import numpy as np

def process_img(original_image):
    processed_img = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    processed_img = cv2.Canny(processed_img, threshold1=200, threshold2=300)
    processed_img = cv2.resize(processed_img,(80,80))
    processed_img = np.transpose(processed_img, (2, 0, 1))
    processed_img = processed_img.astype('float32') / 255.
    return processed_img
