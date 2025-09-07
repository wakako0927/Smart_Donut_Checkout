import cv2
from ultralytics import YOLO
import os

# ドーナツ
PRICES = {
    "angel_cream": 151,
    "strawberry_french": 172,
    "honey_churro": 140,
    "choco_fashion": 151,
    "honey_dip": 140,
    "pon_de_ring": 140,
}

model = YOLO("donut_checkout_system\models\yolo_donuts.pt")

# ラベル名（YOLOのクラスID）
LABEL_MAP = {
    0: "angel_cream",
    5: "strawberry_french",
    2: "honey_churro",
    1: "choco_fashion",
    3: "honey_dip",
    4: "pon_de_ring",
    6: "unknown",
}

def detect_donuts(image_path):
    image = cv2.imread(image_path)
    results = model.predict(source=image_path, conf=0.4)[0]

    counts = {}

    for box in results.boxes:
        cls_id = int(box.cls[0].item())
        x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())

        # ドーナツ領域
        cropped = image[y1:y2, x1:x2]

        # 二段階推論
        sub_results = model.predict(source=cropped, conf=0.4, imgsz=224)[0]
        if len(sub_results.boxes) > 0:
            sub_cls_id = int(sub_results.boxes[0].cls[0].item())
            label = LABEL_MAP.get(sub_cls_id, "unknown")
        else:
            label = "unknown"

        counts[label] = counts.get(label, 0) + 1

    total = sum(counts.get(k, 0) * PRICES.get(k, 0) for k in counts)
    return {"counts": counts, "total": total}
