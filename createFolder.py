import cv2
import os
import json
import numpy as np
from deepface import DeepFace
from ultralytics import YOLO

# ===================== ROI Loader =====================
def load_roi(filename="roi_config.json"):
    if os.path.exists(filename):
        with open(filename, "r") as f:
            data = json.load(f)
            return np.array(data["roi"], np.int32)
    return None

# ===================== Inside ROI Check =====================
def is_inside_polygon(x, y, polygon):
    if polygon is None:
        return True   # if no ROI, accept all
    return cv2.pointPolygonTest(polygon, (x, y), False) >= 0

# ===================== Duplicate Face Check =====================
def is_duplicate(face_img, known_faces_path):
    try:
        result = DeepFace.find(
            img_path=face_img,
            db_path=known_faces_path,
            model_name="ArcFace",
            enforce_detection=False,
            silent=True
        )
        return len(result) > 0 and not result[0].empty
    except:
        return False

# ===================== Save Face =====================
def save_face(face_crop, save_dir, name):
    os.makedirs(save_dir, exist_ok=True)
    person_folder = os.path.join(save_dir, name)
    os.makedirs(person_folder, exist_ok=True)
    count = len(os.listdir(person_folder))
    file_path = os.path.join(person_folder, f"{count + 1}.jpg")
    cv2.imwrite(file_path, face_crop)
    print(f"✅ Saved: {file_path}")

# ===================== Main =====================
def run_face_capture(video_source=0, roi_file="roi_config.json"):
    roi_polygon = load_roi(roi_file)
    known_faces_base = "face_dataset"
    os.makedirs(known_faces_base, exist_ok=True)

    name = input("Enter the person's name to capture: ").strip()
    if not name:
        print("⚠️ No name entered. Exiting.")
        return

    # Open webcam or video
    if isinstance(video_source, str) and os.path.exists(video_source):
        cap = cv2.VideoCapture(video_source)
    else:
        cap = cv2.VideoCapture(0)

    model = YOLO("yolov11n-face.pt")
    frame_skip = 5
    frame_count = 0

    print(f"📸 Capturing faces for {name}... Press 'q' to stop.")

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame_count += 1
        if frame_count % frame_skip != 0:
            continue

        results = model(frame)

        for result in results:
            for box in result.boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                face_center = ((x1 + x2) // 2, (y1 + y2) // 2)

                if not is_inside_polygon(*face_center, roi_polygon):
                    continue

                face_crop = frame[y1:y2, x1:x2]
                if face_crop.size == 0 or face_crop.shape[0] < 50 or face_crop.shape[1] < 50:
                    continue

                save_face(face_crop, known_faces_base, name)

        cv2.imshow(f"Capturing Faces for {name}", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    print(f"✅ Face capture complete for {name}!")

# Run
if __name__ == "__main__":
    run_face_capture(video_source=0)
