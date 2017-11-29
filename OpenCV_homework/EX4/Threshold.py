# Copyright 2017 Keval Khara kevalk@bu.edu

import cv2

img = cv2.imread('baboon.jpg')	# read an image
cv2.imshow('original.jpg',img)

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)	# convert to grayscale

[ret,threshold] = cv2.threshold(gray, 128, 255,2)
cv2.imshow('Thresholded',threshold)
cv2.imwrite('Thresholded.jpg',threshold)	# thresholded image

[ret, binary_thresh] = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)
cv2.imshow('Binary Threshold',binary_thresh)
cv2.imwrite('Binary_Threshold.jpg',binary_thresh)	# binary threshold

[ret,thresh1] = cv2.threshold(gray,125,255,cv2.THRESH_BINARY_INV)
[ret, thresh2] = cv2.threshold(gray, 27, 255, cv2.THRESH_BINARY)

band_thresh = cv2.bitwise_and(thresh1,thresh2)
cv2.imshow('Banded Threshold',band_thresh)
cv2.imwrite('Banded_Threshold.jpg',band_thresh)	# band threshold

[ret,thresh3] = cv2.threshold(gray,128,255,cv2.THRESH_BINARY_INV|cv2.THRESH_OTSU)
semi_thresh = cv2.bitwise_and(gray,thresh3)
cv2.imshow('Semi-Thresholded',semi_thresh)
cv2.imwrite('Semi-Threshold.jpg',semi_thresh)	# semi threshold

adaptive_thresh = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,101,10)
cv2.imshow('Adaptive Threshold', adaptive_thresh)
cv2.imwrite('Adaptive_Threshold.jpg', adaptive_thresh)	# adaptive threshold

cv2.waitKey(0)
