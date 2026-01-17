import cv2
import numpy as np

def edge_density(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        return 0.0

    edges = cv2.Canny(img, 100, 200)

    edge_pixels = np.count_nonzero(edges)
    total_pixels = edges.size

    return edge_pixels / total_pixels 

def background_issue(edge_density_value):
    if edge_density_value > 0.15:
        return "cluttered_background"
    return None
