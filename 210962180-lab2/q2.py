import cv2
import numpy as np
import matplotlib.pyplot as plt
def histogram_specification(input_image_path, reference_image_path, output_image_path):
    # Load the input and reference images
    input_image = cv2.imread(input_image_path, cv2.IMREAD_GRAYSCALE)
    reference_image = cv2.imread(reference_image_path, cv2.IMREAD_GRAYSCALE)

    if input_image is None or reference_image is None:
        print("Error: Could not load the images.")
        return

    # Calculate histograms of input and reference images
    input_hist, _ = np.histogram(input_image.flatten(), bins=256, range=[0, 256])
    reference_hist, _ = np.histogram(reference_image.flatten(), bins=256, range=[0, 256])

    # Calculate cumulative histograms
    input_cdf = input_hist.cumsum()
    reference_cdf = reference_hist.cumsum()

    # Normalize cumulative histograms
    input_cdf_normalized = (input_cdf - input_cdf.min()) / (input_cdf.max() - input_cdf.min()) * 255
    reference_cdf_normalized = (reference_cdf - reference_cdf.min()) / (reference_cdf.max() - reference_cdf.min()) * 255

    # Create a lookup table for histogram specification
    lookup_table = np.interp(input_cdf_normalized, reference_cdf_normalized, np.arange(256))

    # Apply the lookup table to the input image
    output_image = cv2.LUT(input_image, lookup_table)

    # Save the output image
    cv2.imwrite(output_image_path, output_image)
    print("Histogram specification completed and saved!")


if __name__ == "__main__":
    input_image_path = "r.jpg"  # Change this to the path of your input image
    reference_image_path = "y.jpg"  # Change this to the path of your reference image
    output_image_path = "output_image.jpg"  # Change this to the desired output path

    histogram_specification(input_image_path, reference_image_path, output_image_path)