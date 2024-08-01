import cv2
import numpy as np
from matplotlib import pyplot as plt

    

def get_new_frame_size_and_matrix(homography_matrix, second_image_shape, base_image_shape):

     # Reading the size of the image
    (height, width) = second_image_shape
    
    # Taking the matrix of initial coordinates of the corners of the secondary image
    # Stored in the following format: [[x1, x2, x3, x4], [y1, y2, y3, y4], [1, 1, 1, 1]]
    # Where (xi, yi) is the coordinate of the i th corner of the image. 
    initial_matrix = np.array([[0, width - 1, width - 1, 0], [0, 0, height - 1, height - 1], [1, 1, 1, 1]])
    

    # Finding the final coordinates of the corners of the image after transformation.
    # NOTE: Here, the coordinates of the corners of the frame may go out of the 
    # frame(negative values). We will correct this afterwards by updating the 
    # homography matrix accordingly.
    final_matrix = np.dot(homography_matrix, initial_matrix)

    [x, y, c] = final_matrix
    x = np.divide(x, c)
    y = np.divide(y, c)

    # Finding the dimentions of the stitched image frame and the "correction" factor
    min_x, max_x = int(round(min(x))), int(round(max(x)))
    min_y, max_y = int(round(min(y))), int(round(max(y)))

    new_width = max_x
    new_height = max_y
    correction = [0, 0]
    if min_x < 0:
        new_width -= min_x
        correction[0] = abs(min_x)
    if min_y < 0:
        new_height -= min_y
        correction[1] = abs(min_y)
    
    # Again correcting new_width and new_height
    # Helpful when secondary image is overlaped on the left hand side of the Base image.
    if new_width < base_image_shape[1] + correction[0]:
        new_width = base_image_shape[1] + correction[0]
    if new_height < base_image_shape[0] + correction[1]:
        new_height = base_image_shape[0] + correction[1]

    # Finding the coordinates of the corners of the image if they all were within the frame.
    x = np.add(x, correction[0])
    y = np.add(y, correction[1])
    old_initial_points = np.float32([[0, 0],
                                   [width - 1, 0],
                                   [width - 1, height - 1],
                                   [0, height - 1]])
    new_final_points = np.float32(np.array([x, y]).transpose())

    # Updating the homography matrix. Done so that now the secondary image completely 
    # lies inside the frame
    homography_matrix = cv2.getPerspectiveTransform(old_initial_points, new_final_points)
    
    return [new_height, new_width], correction, homography_matrix
