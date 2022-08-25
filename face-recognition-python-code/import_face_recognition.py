#To install the numpy opencv-python
#pip install numpy opencv-python  
#To install the face_recognition, install the dlib package first.  
#pip install dlib  
#To install face_recognition module using the below command.  
#pip install face_recognition


#import the necessary modules
import face_recognition as fr
import cv2

import numpy as np
import os

#create 2 lists that store the names of the images (persons) and their respective face encodings.

path = "C:/Users/cindy/Python_activity1/face-recognition-python-code/train//"

known_names = []
known_name_encodings = []

images = os.listdir(path)


#loop through each of the images in our train directory, extract the name of the person in the image
#calculate its face encoding vector and store the information in the respective lists.

for _ in images:
 image = fr.load_image_file(path + _)
image_path = path + _
encoding = fr.face_encodings(image)[0]

known_name_encodings.append(encoding)
known_names.append(os.path.splitext(os.path.basename(image_path))[0].capitalize())

#Read the test image using the cv2 imread() method.

test_image = "C:/Users/cindy/Python_activity1/face-recognition-python-code/test/test.jpg"

image = cv2.imread(test_image)

#The face_recognition library provides a useful method
#method called face_locations() which locates the coordinates (left, bottom, right, top) of every face detected in the image. 

face_locations = fr.face_locations(image)

face_encodings = fr.face_encodings(image, face_locations)

#loop through each of the face locations and its encoding found in the image. 
#compare this encoding with the encodings of the faces from the “train” dataset.
#pick the minimum valued distance from it indicating that this face of the test image is one of the persons from the training dataset
#draw a rectangle with the face location coordinates using the methods from the cv2 module.

for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
   matches = fr.compare_faces(known_name_encodings, face_encoding)
   name = ""

   face_distances = fr.face_distance(known_name_encodings, face_encoding)
   best_match = np.argmin(face_distances)

   if matches[best_match]:
       name = known_names[best_match]

   cv2.rectangle(image, (left, top), (right, bottom), (0, 0, 255), 2)
   cv2.rectangle(image, (left, bottom - 15), (right, bottom), (0, 0, 255), cv2.FILLED)

   font = cv2.FONT_HERSHEY_DUPLEX
   cv2.putText(image, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
   
   #Display the image using the imshow() method of the cv2 module.
   cv2.imshow("Result", image)
   
   #Save the image to our current working directory using the imwrite() method.
   cv2.imwrite("./output.jpg", image)
   
   #Release the resources that weren’t deallocated(if any)
   cv2.waitKey(0)
   cv2.destroyAllWindows()
