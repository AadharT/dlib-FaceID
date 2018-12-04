import cv2
import face_recognition
import numpy as np

# Take the users name as the input
person_name = input("Enter your name: ")


# Capture frames from the default camera
cam = cv2.VideoCapture(0)

cv2.namedWindow("capture")

# Define the image counter for variable number of images
img_counter = 0

while img_counter<1:
    ret, frame = cam.read()
    cv2.imshow("capture", frame)

    if not ret:
        break
    k = cv2.waitKey(1)

    if k%256 == 27:
    # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
    # SPACE pressed
        # Learn to recognize the particular frame
        frame_face_encoding = face_recognition.face_encodings(frame)[0]
        data = np.array(frame_face_encoding)
        np.save('known/'+person_name, data)

        img_counter += 1

cam.release()

cv2.destroyAllWindows()
