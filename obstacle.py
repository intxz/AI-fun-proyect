import cv2

def process_image(img):
    _, img = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)  # Convert to black & white
    contours, _ = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    obstacle_distance = None
    obstacle_height = None

    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        if x > 50:  # Ignore the dino itself
            obstacle_distance = x
            obstacle_height = h
            break  # Only consider the nearest obstacle

    return obstacle_distance, obstacle_height

od, oh = process_image("pruebadino.PNG")
print(od)
print(oh)