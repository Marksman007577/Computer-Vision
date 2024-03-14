import cv2
# Select a ROI and then press SPACE or ENTER button!
# Cancel the selection process by pressing c button!
# create an instance of a tracker
tracker = cv2.TrackerKCF_create()

video = cv2.VideoCapture('race.mp4')
ok, frame = video.read()

bounding_box = cv2.selectROI(frame)
ok = tracker.init(frame, bounding_box)

while True:
    ok, frame = video.read()
    if not ok:
        break
    ok, bounding_box = tracker.update(frame)

    if ok:
        (x_coor, y_coor, width, height) = [int(v) for v in bounding_box]
        cv2.rectangle(frame, (x_coor, y_coor), (x_coor + width, y_coor + height), (0, 255, 0), 2, 1)
    else:
        cv2.putText(frame, 'Error', (100, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.imshow('Tracking', frame)

    if cv2.waitKey(1) & 0xFF == 27:     # Esc key on keyboard
        break
