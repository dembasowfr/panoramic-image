import cv2
import numpy as np
from matplotlib import pyplot as plt

      
def find_homography(matches, base_image_kp, second_image_kp):
    
    # If less than 4 matches found, exit the code.
    if len(matches) < 4:
        print("\nNot enough matches found between the 2 images.\n")
        exit(0)

    # Storing coordinates of points corresponding to the matches found in both the images
    base_image_pts = []
    second_image_pts = []
    for match in matches:
        base_image_pts.append(base_image_kp[match[0].queryIdx].pt)
        second_image_pts.append(second_image_kp[match[0].trainIdx].pt)

    # Changing the datatype to "float32" for finding homography
    base_image_pts = np.float32(base_image_pts)
    second_image_pts = np.float32(second_image_pts)

    # Finding the homography matrix(transformation matrix).
    (homographic_matrix, static) = cv2.findHomography(second_image_pts, base_image_pts, cv2.RANSAC, 4.0)

    return homographic_matrix, static
