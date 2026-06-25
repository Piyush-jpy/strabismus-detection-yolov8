from ultralytics import YOLO

CLASS_NAMES = {
    0: 'Eso Down Left',
    1: 'Eso Down Right',
    2: 'Eso Left',
    3: 'Eso Right',
    4: 'Eso Straight Ahead',
    5: 'Eso Straight Down',
    6: 'Eso Straight Up',
    7: 'Eso Up Left',
    8: 'Eso Up Right',
    9: 'Exo Down Left',
    10: 'Exo Down Right',
    11: 'Exo Right',
    12: 'Exo Straight Ahead',
    13: 'Exo Straight Down',
    14: 'Exo Straight Up',
    15: 'Exo Up Left',
    16: 'Exo Up Right',
    17: 'Exo Left',
    18: 'Hyper Down Left',
    19: 'Hyper Down Right',
    20: 'Hyper Left',
    21: 'Hyper Right',
    22: 'Hyper Straight Ahead',
    23: 'Hyper Straight Down',
    24: 'Hyper Up Left',
    25: 'Hypo Down Left',
    26: 'Hypo Down Right',
    27: 'Hypo Left',
    28: 'Hypo Right',
    29: 'Hypo Straight Ahead',
    30: 'Hypo Straight Down',
    31: 'Hypo Straight Up',
    32: 'Hypo Up Left',
    33: 'Hypo Up Right',
    34: 'Normal Down Left',
    35: 'Normal Down Right',
    36: 'Normal Left',
    37: 'Normal Right',
    38: 'Normal Straight Ahead',
    39: 'Normal Straight Down',
    40: 'Normal Straight Up',
    41: 'Normal Up Left',
    42: 'Normal Up Right'
}

MODEL_PATH = "best.pt"
IMAGE_PATH = "sample.jpg"

def main():
    model = YOLO(MODEL_PATH)

    results = model(IMAGE_PATH)

    if len(results[0].boxes.cls) > 0:
        cls_id = int(results[0].boxes.cls[0].item())
        confidence = float(results[0].boxes.conf[0].item())

        print(f"Prediction: {CLASS_NAMES[cls_id]}")
        print(f"Confidence: {confidence:.4f}")
    else:
        print("No detection found.")

if __name__ == "__main__":
    main()