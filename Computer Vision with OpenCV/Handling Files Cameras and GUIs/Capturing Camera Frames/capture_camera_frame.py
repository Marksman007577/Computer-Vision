import cv2

camera_capture = cv2.VideoCapture(0)
frame_per_sec = 30  # Assumed number
CAPT_TIME = 10

size = (int(camera_capture.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(camera_capture.get(cv2.CAP_PROP_FRAME_HEIGHT)))

video_writer = cv2.VideoWriter("output.avi", cv2.VideoWriter_fourcc(*'XVID'),
                               frame_per_sec, size)

success, frame = camera_capture.read()
num_frame_remaining = CAPT_TIME * frame_per_sec - 1
while success and num_frame_remaining > 0:
    video_writer.write(frame)
    success, frame = camera_capture.read()
    num_frame_remaining -= 1
