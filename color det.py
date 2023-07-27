import cv2
import numpy as np

def detect_color(image, lower_range, upper_range):
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv_image, lower_range, upper_range)
    result = cv2.bitwise_and(image, image, mask=mask)
    return result

def main():
    # Replace 'path_to_image.jpg' with the path to your sample image
    image = cv2.imread('ggg.jpg')
    
    # Define the lower and upper color ranges (example: red color range)
    lower_red = np.array([0, 100, 100])  # HSV values for lower red color
    upper_red = np.array([10, 255, 255])  # HSV values for upper red color
    
    # Detect the color
    color_detected = detect_color(image, lower_red, upper_red)

    # Display the original image and the color-detected image side by side
    cv2.imshow("Original Image", image)
    cv2.imshow("Color Detected", color_detected)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
