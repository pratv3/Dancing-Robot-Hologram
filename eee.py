# this is only for test
"""
only for practising the code
"""
# aim is to build a pose skeleton tracker using python
import cv2
import mediapipe as tflow
import numpy as np
skeleton=tflow.solutions.pose
s_draw=tflow.solutions.drawing_utils
img_est=skeleton.Pose()
vid=cv2.VideoCapture("sample.mp4")
while True:
    frame,img=vid.read()
    cvtimg=cv2.resize(img,(600,400))
    pros_img=img_est.process(cvtimg)
    a,b,c=img.shape
    opimg=np.zeros([a,b,c])
    s_draw.draw_landmarks(opimg,pros_img.pose_landmarks,skeleton.POSE_CONNECTIONS)
    cv2.imshow("Dancing robot hologram",opimg)
    key=cv2.waitKey(1)
    if key==ord("q"):
        vid.release()
        cv2.destroyAllWindows()