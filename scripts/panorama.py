import cv2
import numpy as np
from matplotlib import pyplot as plt


from .matches import find_matches
from .homography import find_homography
from .correction import get_new_frame_size_and_matrix



def stitch_images(base_image, second_image):

    # Finding matches between the 2 images and their keypoints
    matches, base_image_kp, second_image_kp = find_matches(base_image, second_image)
    
    # Finding homography matrix.
    homography_matrix, status = find_homography(matches, base_image_kp, second_image_kp)
    
    # Finding size of new frame of stitched images and updating the homography matrix 
    new_frame_size, correction, homography_matrix = get_new_frame_size_and_matrix(homography_matrix, second_image.shape[:2], base_image.shape[:2])
    

    # Finally placing the images upon one another.
    panorama = cv2.warpPerspective(second_image, homography_matrix, (new_frame_size[1], new_frame_size[0]))
    panorama[correction[1]:correction[1]+base_image.shape[0], correction[0]:correction[0]+base_image.shape[1]] = base_image

    return panorama