from ultralytics import YOLO

MODEL = "yolov8n.pt"
DATASET_YAML = "data.yaml"

def main():
    model = YOLO(MODEL)

    model.train(
        data=DATASET_YAML,
        epochs=100,
        imgsz=640
    )

if __name__ == "__main__":
    main()