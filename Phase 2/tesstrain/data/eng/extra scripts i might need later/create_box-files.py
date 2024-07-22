import os
from PIL import Image
import pytesseract

# Path to your ground truth directory
ground_truth_dir = './eng_betway_model-ground-truth/'

# Function to create box files for images in a directory
def create_box_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.tiff') or filename.endswith('.tif'):  # Adjust file extension as needed
            image_path = os.path.join(directory, filename)
            txt_path = os.path.join(directory, filename.replace('.tiff', '.txt').replace('.tif', '.txt'))

            # Use pytesseract to get bounding boxes and text
            boxes_data = pytesseract.image_to_boxes(Image.open(image_path))

            # Write boxes data to a .box file
            with open(txt_path, 'w') as txt_file:
                txt_file.write(boxes_data)

            print(f"Created box file for {filename}")

# Create box files for images in the ground truth directory
create_box_files(ground_truth_dir)
