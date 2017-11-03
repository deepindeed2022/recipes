
import cv2
import sys
# Get user supplied values
imagePath = "./multi_faces.jpg"
# Create the haar cascade
faceCascade = cv2.CascadeClassifier("./haarcascade_frontalface_alt2.xml") 
# Read the image
image = cv2.imread(imagePath)#2
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)#3
# Detect faces in the image
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.15,
    minNeighbors=5,
    minSize=(5,5),
    flags = cv2.cv.CV_HAAR_SCALE_IMAGE
) #4
print "Found {0} faces!".format(len(faces))#5
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2) #6
cv2.imshow("Faces found", image)#7
cv2.waitKey(0) #8