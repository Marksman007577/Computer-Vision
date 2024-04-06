import cv2
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

video_capture = cv2.VideoCapture(0)  # 0 is for the device webcam. 1 is for a first external video device

while True:
    # Capture frame by frame from video
    # frames are typically images per time instance over the duration of a video
    ret, frame = video_capture.read()
    gray_image = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    face_detections = face_detector.detectMultiScale(gray_image, minSize=(100, 100))

    for (x_coor,y_coor,width,height) in face_detections:
        # Draw the bounding box
        print(width,height)
        cv2.rectangle(frame, (x_coor, y_coor), (x_coor+width, y_coor+height), (0, 255, 0), 2)

    # Display the resulting frameq
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# Release the capture after everything is completed
# this help release the machine memory
video_capture.release()
cv2.destroyAllWindows()
