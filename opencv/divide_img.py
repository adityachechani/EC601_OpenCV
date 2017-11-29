import numpy as np
import cv2

def divide_img(src, rows, cols, new_img):
	width = src.shape[0]
	height = src.shape[1]

	print('width: ', width, ' ------ height: ', height)
	dim = [width, height]

	start = [0, 0]
	end = [rows, cols]

	for i in range(0,(width//rows)):
		for j in range(0, (height//cols)):
			s = [start[0], start[1]]
			e = [start[0] + rows, start[1] + cols]
			cv2.rectangle(new_img, (start[0], start[1]), (start[0] + rows, start[1] + cols), (0,0,255), 1)
			cv2.imwrite('NewImage.png', new_img)
			start[0] = start[0] + rows

		start[0] = 0
		start[1] += cols 

	return new_img
source_img = cv2.imread('source_img.jpg',0) # read image in grayscale
new_img = cv2.cvtColor(source_img, cv2.COLOR_GRAY2RGB)
image = divide_img(source_img, 20, 20, new_img)
# print(image)
cv2.namedWindow('SourceImage', cv2.WINDOW_NORMAL)
cv2.imshow('SourceImage', source_img)
cv2.namedWindow('NewImage', cv2.WINDOW_NORMAL)
cv2.imshow('NewImage', image)

part = image[120:160, 160:200]
cv2.namedWindow('PartImage', cv2.WINDOW_NORMAL)
cv2.imshow('PartImage', part)
cv2.waitKey(0)
cv2.destroyAllWindows()
	