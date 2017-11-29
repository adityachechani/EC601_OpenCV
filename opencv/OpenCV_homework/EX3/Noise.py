# Copyright 2017 Keval Khara kevalk@bu.edu

import cv2
import numpy as np

def salt_pepper_noise(img, pa, pb):
    row,col,ch=img.shape
    amount1=row*col*pa   
    amount2=row*col*pb
    for i in range(int(amount1)):
        img[int(np.random.uniform(0,row))][int(np.random.uniform(0,col))]=0
    for i in range(int(amount2)):
        img[int(np.random.uniform(0,row))][int(np.random.uniform(0,col))]=255

def gaussian_noise(img, mean, sigma):
    NoiseArr = img.copy()
    NoiseArr = np.random.normal(mean, sigma, img.shape)
    np.add(img, NoiseArr, img, casting="unsafe")

img=cv2.imread('baboon.jpg')
cv2.imshow('Original', img)

noise_img=img.copy()
mean = 0
sigma = 50
gaussian_noise(noise_img, mean, sigma)
cv2.imshow('Gaussian Noise', noise_img)     # Gaussian Noise
cv2.imwrite('Gaussian Noise.png', noise_img)

noise_dst=noise_img.copy()
cv2.blur(noise_dst,(3,3))
cv2.imshow('Box Filter', noise_dst)     # Box Filter
cv2.imwrite('Box Filter.png', noise_dst)

noise_dst1=noise_img.copy()
cv2.GaussianBlur(noise_dst1,(3,3),1.5)
cv2.imshow('Gaussian Filter', noise_dst1)       # Gaussian Filter
cv2.imwrite('Gaussian Filter.png', noise_dst1)

noise_dst2=noise_img.copy()
cv2.medianBlur(noise_dst2,3)
cv2.imshow('Median Filter', noise_dst2)     # Median Filter
cv2.imwrite('Median Filter.png', noise_dst2)

noise_img2=img.copy()
pa=0.01
pb=0.01
salt_pepper_noise(noise_img2,pa,pb)
cv2.imshow("Salt and Pepper Noise", noise_img2)      # Salt and Pepper Noise
cv2.imwrite('Salt and Pepper Noise.png', noise_img2)

noise_dst3=noise_img2.copy()
cv2.blur(noise_dst3,(3,3))
cv2.imshow('Box Filter 2', noise_dst3)
cv2.imwrite('Box Filter 2.png', noise_dst3)

noise_dst4=noise_img2.copy()
cv2.GaussianBlur(noise_dst4,(3,3),1.5)
cv2.imshow('GaussianBlur Filter 2', noise_dst4)
cv2.imwrite('GaussianBlur Filter 2.png', noise_dst4)

noise_dst5=noise_img2.copy()
cv2.medianBlur(noise_dst5,3)
cv2.imshow('Median Filter 2', noise_dst5)
cv2.imwrite('Median Filter 2.png', noise_dst5)
cv2.waitKey(0)