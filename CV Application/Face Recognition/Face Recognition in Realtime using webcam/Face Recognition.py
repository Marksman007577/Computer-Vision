import cv2

face_detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.read("lbph_classifier.yml")

width, height = 220, 220
font = cv2.FONT_HERSHEY_COMPLEX_SMALL
camera_capture = cv2.VideoCapture(0)

while True:
    connected, image = camera_capture.read()
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    detections = face_detector.detectMultiScale(image_gray, scaleFactor=1.5, minSize=(30,30))
    for (x_coor,y_coor,w,h) in detections:
        image_faces = cv2.resize(image_gray[y_coor:y_coor+w,x_coor:x_coor+h],(width,height))
        cv2.rectangle(image, (x_coor, y_coor),(x_coor+w, y_coor+h), (0, 0, 255), 2)
        id, confidence = face_recognizer.predict(image_faces)
        name = ""
        if id == 1:
            name = "Mark"
        elif id == 2:
            name = "Uche"

        cv2.putText(image, name, (x_coor, y_coor + (w + 30)), font, fontScale=2, color=(0, 0, 255))
        cv2.putText(image, str(confidence), (x_coor, y_coor + (h + 50)), font, fontScale=1, color=(0, 0, 255))

    cv2.imshow("Face", image)
    if cv2.waitKey(1) == ord('q'):
        break

camera_capture.release()

