#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 15:17:39 2019

@author: raj
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt


img1 = np.zeros((512,512,3), np.uint8)
cv2.line(img1, (0,99), (99,0), (0,0,255), 2)
cv2.rectangle(img1, (100, 60), (270, 170), (255,0,0), 2)
cv2.circle(img1, (300,300), 100, (0,255,0), -1)
cv2.ellipse(img1, (150, 250), (50,20), 0, 0, 360, (125,125,125), -1)
points = np.array([[80,2], [125,0], [179,0],[230,5],[30,50]], np.int32)
points = points.reshape((-1,1,2))
cv2.polylines(img1, [points], True, (0,255,255))
text1 = "Sample text"
cv2.putText(img1, text1, (350,350), cv2.FONT_HERSHEY_SIMPLEX, 3, (180,180,180))
plt.imshow(img1)
plt.show()
 