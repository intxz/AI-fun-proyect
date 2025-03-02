import mss
import numpy as np
import cv2

# Define screen capture area (adjust as needed)
capture_area = {"top": 200, "left": 580, "width": 760, "height": 150}

def grab_screen():
    with mss.mss() as sct:
        screenshot = sct.grab(capture_area)
        img = np.array(screenshot)  # Convert to NumPy array
        img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)  # Convert to grayscale
        return img

def process_image(img):
    _, img = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)  # Convert to black & white
    contours, _ = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    obstacle_distance = None
    obstacle_height = None
    dino_area = (150, 0, img.shape[1] - 150, img.shape[0])  # Define area right of dino

    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        if x > 150:  # Ignore the dino itself
            obstacle_distance = x
            obstacle_height = h
            # Draw rectangle around obstacle
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Highlight the area where obstacles are detected
    cv2.rectangle(img, (150, 0), (img.shape[1], img.shape[0]), (255, 0, 0), 2)
    return img, obstacle_distance, obstacle_height

while True:
    frame = grab_screen()
    processed_frame, od, oh = process_image(frame)
    print("distance:", od)
    print("height:", oh)
    cv2.imshow("Dino Game - Detection Zone", processed_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to quit
        break

cv2.destroyAllWindows()
