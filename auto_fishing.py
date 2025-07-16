import cv2
import numpy as np
import pyautogui
import time
import mss
import os

try:
    script_dir = os.path.dirname(__file__)
    template_path = os.path.join(script_dir, 'lmb_template.png')
    
    print(f"Looking for template at: {template_path}")
    
    template = cv2.imread(template_path, cv2.IMREAD_UNCHANGED)
    
    if template is None:
        raise FileNotFoundError("Template file could not be loaded. Check file path, name, and integrity.")
        
    w, h = template.shape[1], template.shape[0]

except Exception as e:
    print(f"Error loading template: {e}")
    print("\nMake sure 'lmb_template.png' is in the same folder as the script.")
    exit()

threshold = 0.8
monitor = {"top": 400, "left": 800, "width": 400, "height": 300}

print("Auto-Fisher Program Started. Press Ctrl+C in the terminal to stop.")

with mss.mss() as sct:
    while True:
        try:
            screen_img_raw = sct.grab(monitor)
            screen_img = np.array(screen_img_raw)
            
            screen_gray = cv2.cvtColor(screen_img, cv2.COLOR_BGRA2GRAY)
            template_gray = cv2.cvtColor(template, cv2.COLOR_BGRA2GRAY)

            result = cv2.matchTemplate(screen_gray, template_gray, cv2.TM_CCOEFF_NORMED)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

            if max_val >= threshold:
                print(f"LMB icon detected! (Confidence: {max_val:.2f}) - Clicking...")
                
                pyautogui.click()
                time.sleep(0.5)
                pyautogui.click()
                time.sleep(0.5)
                pyautogui.click()
                
                time.sleep(1) 
            
            time.sleep(0.1)

        except KeyboardInterrupt:
            print("Program stopped.")
            break
        except Exception as e:
            print(f"An error occurred during the loop: {e}")
            time.sleep(1)