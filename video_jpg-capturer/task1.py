import uuid
import cv2

video = r'C:\Users\Legion\Desktop\staj_ayvos\stuff\test_video.mp4' #required video path comes here#
req_folder = r'C:\Users\Legion\Desktop\staj_ayvos\stuff' #output path for jpgs#
frame_count = 0

frame_cut = cv2.VideoCapture(video)

while frame_cut.isOpened():
    ret, frame = frame_cut.read()

    if not ret:
        break
    frame_count += 1

    if frame_count % 3 == 0:
        capture_id = str(uuid.uuid4())
        capture_path = req_folder + '\\' + capture_id + '.jpg'
        cv2.imwrite(capture_path, frame)

frame_cut.release()
cv2.destroyAllWindows()
