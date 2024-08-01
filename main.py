import cv2
import numpy as np
from matplotlib import pyplot as plt
import os
from scripts.panorama import stitch_images


if __name__ == "__main__":
 

    # Load the images
    # Use absolute paths for debugging purposes
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), './data'))
    image1_path = os.path.join(root_dir, 'input', 'soru_2_gorsel1.png')
    image2_path = os.path.join(root_dir, 'input', 'soru_2_gorsel2.png')
    output_image_path = os.path.join(root_dir, 'output', 'panorama.jpg')

    # Print the full paths for debugging
    print(f"Image 1 path: {image1_path}")
    print(f"Image 2 path: {image2_path}")
    print(f"Output image path: {output_image_path}")

    # Load the images
    image1 = cv2.imread(image1_path)
    image2 = cv2.imread(image2_path)
    if image1 is None:
        raise FileNotFoundError(f"Failed to load image: {image1_path}")
    if image2 is None:
        raise FileNotFoundError(f"Failed to load image: {image2_path}")


    # Checking if images read
    if image1 is None or image2 is None:
        print("\nImages not read properly or does not exist.\n")
        exit(0)

    # Calling function for stitching images.
    panorama = stitch_images(image1, image2)

    # Saving the stitched image.
    cv2.imwrite(output_image_path, panorama)

    # Displaying the stitched images.
    plt.imshow(panorama)
    plt.show()
    

    
    