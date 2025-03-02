import mss
import numpy as np
import cv2

# Define screen capture area (adjust as needed)
capture_area = {"top": 300, "left": 400, "width": 600, "height": 200}

def grab_screen():
    with mss.mss() as sct:
        screenshot = sct.grab(capture_area)
        img = np.array(screenshot)  # Convert to NumPy array
        img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)  # Convert to grayscale
        return img

# Test screen capture
while True:
    frame = grab_screen()
    cv2.imshow("Dino Game", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to quit
        break

cv2.destroyAllWindows()
