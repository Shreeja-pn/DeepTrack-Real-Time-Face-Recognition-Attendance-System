import cv2
import json
import numpy as np

# === CONFIG ===
VIDEO_PATH = "None"       # Video file (set to None if using webcam)
FRAME_NUMBER = 100               # Frame to grab from video
OUTPUT_JSON = "roi_config.json"  # Output JSON file

# === Global variables ===
roi_points = []

def mouse_callback(event, x, y, flags, param):
    global roi_points
    if event == cv2.EVENT_LBUTTONDOWN:
        roi_points.append((x, y))
    elif event == cv2.EVENT_RBUTTONDOWN and roi_points:
        roi_points.pop()

def draw_roi(frame, points):
    for point in points:
        cv2.circle(frame, point, 5, (0, 255, 0), -1)
    if len(points) > 1:
        cv2.polylines(frame, [np.array(points)], isClosed=True, color=(255, 0, 0), thickness=2)

def save_roi(points, filename):
    data = {"roi": points}
    with open(filename, "w") as f:
        json.dump(data, f)
    print(f"[✔] ROI saved to {filename}")

def main():
    global roi_points

    # --- Choose source: Webcam or Video ---
    if VIDEO_PATH and VIDEO_PATH.strip().lower() != "none":
        cap = cv2.VideoCapture(VIDEO_PATH)
        if not cap.isOpened():
            print("❌ Error: Could not open video file.")
            return
        cap.set(cv2.CAP_PROP_POS_FRAMES, FRAME_NUMBER)
        ret, frame = cap.read()
    else:
        cap = cv2.VideoCapture(0)  # webcam
        if not cap.isOpened():
            print("❌ Error: Could not open webcam.")
            return
        print("▶ Press SPACE to capture frame for ROI selection.")
        while True:
            ret, live_frame = cap.read()
            if not ret:
                continue
            cv2.imshow("Webcam - Press SPACE to capture", live_frame)
            key = cv2.waitKey(1) & 0xFF
            if key == 32:  # space bar
                frame = live_frame.copy()
                break
            elif key == ord("q"):
                cap.release()
                cv2.destroyAllWindows()
                return
        cap.release()

    if frame is None:
        print("❌ Error: Could not grab frame.")
        return

    print("👉 Left click = add points, Right click = remove last point")
    print("👉 Press 's' = save ROI, 'q' = quit without saving")

    cv2.namedWindow("Draw ROI")
    cv2.setMouseCallback("Draw ROI", mouse_callback)

    while True:
        display_frame = frame.copy()
        draw_roi(display_frame, roi_points)
        cv2.imshow("Draw ROI", display_frame)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('s') and len(roi_points) >= 3:
            save_roi(roi_points, OUTPUT_JSON)
            break
        elif key == ord('q'):
            break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
