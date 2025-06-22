import cv2

cap = cv2.VideoCapture(0)  # 0 is the default camera

if not cap.isOpened():
    print("Cannot open camera")
    exit()

def get_camera_image(show_window=False):
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        return None

    if show_window:
        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            return None

    return frame

if __name__ == "__main__":
    while True:
        if type(get_camera_image(True)) == type(None):
            break

    cap.release()
    cv2.destroyAllWindows()