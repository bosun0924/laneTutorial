import cv2
import numpy as np

def canny(image):
    lane_image = np.copy(image)
    gray = cv2.cvtColor(lane_image, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    canny = cv2.Canny(blur, 50, 150)
    return canny

def region_of_interest(image):
    height = image.shape[0]
    polygons = np.array([
        [(200, height), (1100, height), (550, 250)]
    ])#get the polygon array
    mask = np.zeros_like(image)#make a black mask of the size of the image
    cv2.fillPoly(mask, polygons, 128)
    return mask

    
image = cv2.imread('test_image.jpg')
cropped_image = region_of_interest(canny(image))#get a image of the road(cropped for the road part)
#using hough transformation
lines = cv2.HoughLinesP(cropped_image, 2, np.pi/180, 100, np.array([]), minLineLength = 40, maxLineGap = 5),
#2 as size of the 'bins', 100 as the threshold of the votes
#a line has to atleast has 40 pixels and the gap between segments should not exceed 5 pixels
cv2.imshow('result', region_of_interest(canny(image)))
cv2.waitKey(0)



