from vision.object_detection import detect_objects
from vision.ocr import extract_text
from vision.quality_metrics import blur_score, brightness
from vision.background_analysis import edge_density
from vision.quality_interpretation import (
    interpret_blur,
    interpret_brightness,
    interpret_edge_density,
    compute_quality_score
)
from llm.reasoning import reason
import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def run_pipeline(image_rel_path):
    image_path = os.path.join(BASE_DIR, image_rel_path)

    if not os.path.exists(image_path):
        raise FileNotFoundError(image_path)

    
    blur_val = blur_score(image_path)
    brightness_val = brightness(image_path)
    edge_val = edge_density(image_path)

    
    is_blurry, blur_issue = interpret_blur(blur_val)
    brightness_flag, brightness_issue = interpret_brightness(brightness_val)
    background_flag, background_issue = interpret_edge_density(edge_val)


    quality_score = compute_quality_score(
        is_blurry,
        brightness_flag,
        background_flag
    )

    
    features = {
        "blur_score": blur_val,
        "brightness": brightness_val,
        "edge_density": edge_val,
        "image_quality_score": quality_score,
        "issues_detected": list(
            filter(None, [blur_issue, brightness_issue, background_issue])
        ),
        "detected_objects": detect_objects(image_path),
        "text_detected": extract_text(image_path)
    }

    result = reason(features)

    os.makedirs("outputs", exist_ok=True)
    out_path = f"outputs/{os.path.basename(image_path)}.json"

    with open(out_path, "w") as f:
        json.dump(result, f, indent=2)

    print("Saved →", out_path)

if __name__ == "__main__":
    run_pipeline("examples/e4.webp")
