import cv2
import numpy as np

def blur_score(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        return 0.0
    return cv2.Laplacian(img, cv2.CV_64F).var()

def is_blurry(blur_score, threshold=150):
    """
    Below threshold = blurry
    Above threshold = sharp
    """
    return blur_score < threshold


def brightness(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        return 0.0
    return float(img.mean())


def brightness_issue(brightness_value):
    if brightness_value < 60:
        return "too_dark"
    elif brightness_value > 200:
        return "too_bright"
    return None
