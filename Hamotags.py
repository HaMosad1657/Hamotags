# USAGE: This code detects apriltags and estimates thier pose, giving us the exact position of the camera relative to the tag
# IMPORTANT: this code  

import pupil_apriltags
import cv2
import numpy as np

cap = cv2.VideoCapture(0)
detector = pupil_apriltags.Detector()

while True:
    ret, frame = cap.read()

    cameraParameters = [640, 360, 0.0, 0.0] # fx, fy, cx, cy

    image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    result = detector.detect(image, estimate_tag_pose = True, camera_params = [640, 360, 0.0, 0.0],tag_size= 0.19)
    if len (result) > 0:
        #get corners in pixels
        corner0 = result[0].corners[0]
        DetectedCorner0PX = np.round(corner0).astype(int)
        corner1 = result[0].corners[1]
        DetectedCorner1PX = np.round(corner1).astype(int)
        corner2 = result[0].corners[2]
        DetectedCorner2PX = np.round(corner2).astype(int)
        corner3 = result[0].corners[3]
        DetectedCorner3PX = np.round(corner3).astype(int)
        #get center in pixels
        DetectedCenter = result[0].center
        DetectedCenterPX = np.round(DetectedCenter).astype(int)

        cv2.circle(frame, DetectedCenterPX, 2, (255, 0, 0), 2)

        cv2.line(frame, DetectedCorner0PX, DetectedCorner1PX, (255, 255, 0), 2)
        cv2.line(frame, DetectedCorner1PX, DetectedCorner2PX, (255, 255, 0), 2)
        cv2.line(frame, DetectedCorner2PX, DetectedCorner3PX, (255, 255, 0), 2)
        cv2.line(frame, DetectedCorner3PX, DetectedCorner0PX, (255, 255, 0), 2)
        
        print (result[0].pose_t[1])
    cv2.imshow("Image", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break