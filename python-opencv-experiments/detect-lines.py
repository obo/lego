import numpy as np
import cv2
import argparse
 
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

# load the image, clone it for output, and then convert it to grayscale
img = cv2.imread(args["image"])

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50,150,apertureSize = 3)
print img.shape[1]
print img.shape
minLineLength=img.shape[1]-300
lines = cv2.HoughLinesP(image=edges,rho=0.02,theta=np.pi/500, threshold=10,lines=np.array([]), minLineLength=minLineLength,maxLineGap=100)

a,b,c = lines.shape
for i in range(a):
    #cv2.line(img, (lines[i][0][0], lines[i][0][1]), (lines[i][0][2], lines[i][0][3]), (0, 0, 255), 3, cv2.LINE_AA)
    cv2.line(img, (lines[i][0][0], lines[i][0][1]), (lines[i][0][2],
    lines[i][0][3]), (0, 0, 255), 3, cv2.CV_AA)


cv2.imshow('edges', edges)
cv2.imshow('result', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
