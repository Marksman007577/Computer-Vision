import cv2

# Capture frames from video
video_capture = cv2.VideoCapture("race.mp4")

frame_per_sec = video_capture.get(cv2.CAP_PROP_FPS)
size = (int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
        )

print(frame_per_sec)
print(size)

# Write the frames from captured video into another video file format
video_writer = cv2.VideoWriter("race_output.avi",
                               cv2.VideoWriter_fourcc('X','V','I','D'),
                               frame_per_sec,
                               size)

success, frame = video_capture.read()
while success:
    video_writer.write(frame)
    success, frame = video_capture.read()

# close all video files or capturing device
video_capture.release()
