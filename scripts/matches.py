import cv2
import numpy as np
from matplotlib import pyplot as plt


def find_matches(base_image, second_image):
  
  # Using SIFT to find the keypoints and decriptors in the images
  sift = cv2.SIFT_create()
  base_image_kp, base_image_des = sift.detectAndCompute(cv2.cvtColor(base_image, cv2.COLOR_BGR2GRAY), None)
  second_image_kp, second_image_des = sift.detectAndCompute(cv2.cvtColor(second_image, cv2.COLOR_BGR2GRAY), None)


  # Using Brute Force matcher to find matches.
  bf_matcher = cv2.BFMatcher()
  initial_matches = bf_matcher.knnMatch(base_image_des, second_image_des, k=2)

  # Applying ratio test and filtering out the good matches.
  good_matches = []
  for m, n in initial_matches:
    if m.distance < 0.75 * n.distance:
      good_matches.append([m])

  return good_matches, base_image_kp, second_image_kp