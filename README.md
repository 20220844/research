# research
Face-recognition

What is Python used for? I was asking myself, that is my concern. Then, I searched Google.

Python can be usde for:   
.AI and machine learning,  
.Data analytics,  
.Data visualisation, 
.Programming applications,  
.Web development,   
.Game development,   
.Language development,   
.Finance,   
.SEO (search engine optmisation),   
.Design  

Suddenly, "Face-recognition" came into view. That is an interesting project which I desired to give insight into.
It is a machine learning model that recofnizes the persons from an image.
The method is used to locate features in the image that are uniquely specified.
Face recognition involves 3 steps: face detection, feature extraction, face recognition.
In this project, we use the face_recognition API and OpenCV.

Tools and Libraries  
*Python-3.x  
*cv2-4.5.2  
*numpy-1.20.3  
*face_recognition-1.3.0 

Steps to develop face recognition model  
1. Prepare the dataset - to create 2 directories, "train" and "test". "train" is to save the images you picked, "test" is for you to choose a picture containning all the images in "train".  
2. Train the model  
3. Test the model on the test dataset  
4. Python face recognitionk output  

Details will be shown in Python file for coding. I have also showed the output in repository but it seems not quite successful. The computer only recognized one person out of six in the picture. Problems came out. Why? Google search again. 

Reasons may be as follows,  
1. Windows is not offically supported this face_recogniton model, as mentioned it might work.  
2. The images that selected do not show the features of the faces well enouth for the classifier. The funny thing is that I tried to recognize the people in the picture by myself but it is even a bit difficult for me to distinguish each other, haha...  
3. My friend reminded me to check the CPU usage while running the program, maybe there was not enough memory. I tried it, it showed 26% which looked good.   

So, it is still a chanllege for me to seek the resolution. Anyway, it is really a fantastic experience to explore an uncharted territory.
