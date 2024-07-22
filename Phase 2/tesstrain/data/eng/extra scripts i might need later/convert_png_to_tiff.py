

from PIL import Image
import os

# Define the directory containing your PNG images
input_dir = "./images"
output_dir = "./eng_betway_model-ground-truth"

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

for file_name in os.listdir(input_dir):
    if file_name.endswith(".png"):
        img_path = os.path.join(input_dir, file_name)
        img = Image.open(img_path)
        
        # Convert to grayscale (8 bpp)
        img = img.convert("L")

        # Convert to 1 bpp (black and white)
        img = img.point(lambda x: 0 if x < 128 else 255, '1')
        
        # Save as TIFF
        base_name = os.path.splitext(file_name)[0]
        tiff_path = os.path.join(output_dir, base_name + ".tif")
        img.save(tiff_path, dpi=(300, 300), compression=None)
        print(f"Converted {file_name} to {tiff_path}")
