#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 13:51:37 2019

@author: raj
"""

import cv2
import matplotlib.pyplot as plt

imgpath = "/home/raj/Documents/AI/OpenCV/standard_test_images/lena_color_256.tif"
img = cv2.imread(imgpath, 0)
print(img)
print(img.shape)
print(img.ndim)
print(img.dtype)
print(img.size)
outpath = "/home/raj/Documents/AI/OpenCV/lena_color_256.jpg"
cv2.imwrite(outpath, img)
plt.imshow(img, cmap='gray')
plt.show()
