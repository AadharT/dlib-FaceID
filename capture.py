import cv2
import face_recognition
import numpy as np
import h5py


cam = cv2.VideoCapture(0)

cv2.namedWindow("capture")

img_counter = 0

#Take the users name as the input and store it to file names.txt
person_name = raw_input("Enter your name: ")

text_file = open("known/names.txt", "a+")


while img_counter<5:
    ret, frame = cam.read()
    cv2.imshow("test", frame)
    if not ret:
        break
    k = cv2.waitKey(1)

    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "known/opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
	#writing name of the person to names.txt
	text_file.write(person_name + "\n")
	
        #learn to recognize the particular frame and create an array
        frame_face_encoding = face_recognition.face_encodings(frame)[0]
	
	#writing generated face encoding to hard disk for later use
	with h5py.File('known/knownfaces.h5', 'a') as hf:
		hf.create_dataset("knownfaces",  data=frame_face_encoding)

        #print(frame_face_encoding)
        img_counter += 1

cam.release()

cv2.destroyAllWindows()

text_file.close()
