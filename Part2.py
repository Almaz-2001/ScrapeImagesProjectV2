import cv2
import numpy as np


def preprocess(cloth, cloth_mask):
    # Load the original cloth image
    img = cv2.imread(cloth)

    # Load the cloth mask image
    mask = cv2.imread(cloth_mask, cv2.IMREAD_GRAYSCALE)

    # Create a blue background image with the same shape as the cloth image
    blue_background = np.zeros_like(img)
    blue_background[:] = (255, 0, 0)

    # Convert the cloth mask image to a binary image
    _, binary_mask = cv2.threshold(mask, 127, 255, cv2.THRESH_BINARY)

    # Use the binary mask to select the part of the blue background to replace with the cloth
    blue_background[binary_mask == 0] = img[binary_mask == 0]

    # Save the blue background cloth image
    cv2.imwrite('blue_background_cloth.png', blue_background)

    return blue_background
