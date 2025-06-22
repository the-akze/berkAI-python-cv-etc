import time
import cam_script
import google_ai_interface
from PIL import Image
import base64
from io import BytesIO
import tts
import cv2

def loop():
    print("start")

    print("getting frame")
    frame = cam_script.get_camera_image()
    if type(frame) == type(None):
        print("couldn't get frame")
        return

    print("resizing image... ", end="")
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    print(cam_script.width, cam_script.height)
    resized = Image.fromarray(rgb_frame).resize((320, int(320 * float(cam_script.height) / float(cam_script.width))), Image.Resampling.LANCZOS)
    print("resized!")

    print("making b64... ", end="")
    buffered = BytesIO()
    resized.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue())
    print("made!")

    print("asking google ai abt image...")
    response = google_ai_interface.generate_response_from_image(img_str, "jpeg")
    print(response)

    tts.play_tts(response)


def main():
    print("initialize")
    while True:
        loop()
        print("waiting before next loop")
        time.sleep(3)

if __name__ == "__main__":
    main()