from ultralytics import YOLO

model = YOLO("yolov8n.pt")

def detect_objects(image_path, conf_threshold=0.4):
    results = model(image_path, verbose=False)[0]
    objects = set()

    if results.boxes is None:
        return []

    for box in results.boxes:
        conf = float(box.conf[0])
        if conf >= conf_threshold:
            cls = int(box.cls[0])
            objects.add(results.names[cls])

    return list(objects)
