import cv2
import face_recognition
import numpy as np

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
	
	text_file.write(person_name + "\n")

        #learn to recognize the particular frame and create an array
        frame_face_encoding = face_recognition.face_encodings(frame)[0]
        img_counter += 1

cam.release()

cv2.destroyAllWindows()

#save that array to the hard disk to load later
#yet to change it so that it saves to HDF5 instead of 
np.save('known/person1', frame_face_encoding)

text_file.close()
