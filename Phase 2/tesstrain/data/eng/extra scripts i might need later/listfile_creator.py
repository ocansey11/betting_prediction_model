import os

# Directory containing the ground truth images
ground_truth_dir = "eng_betway_model-ground-truth"
# List file path
list_file_path = "eng_betway_model-list.txt"

# Get all .tif files in the ground truth directory
images = [f for f in os.listdir(ground_truth_dir) if f.endswith(".tif")]

# Create the list file and write image paths
with open(list_file_path, "w") as list_file:
    for image in images:
        list_file.write(f"{ground_truth_dir}/{image}\n")

print(f"List file '{list_file_path}' created with {len(images)} entries.")
