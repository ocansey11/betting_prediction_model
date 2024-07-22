import os

image_dir = './eng_betway_model-ground-truth'  
output_dir = './eng_betway_model-ground-truth'  

# Ensure output directory exists
os.makedirs(output_dir, exist_ok=True)

# Iterate over each image in the directory
for filename in os.listdir(image_dir):
    if filename.endswith('.tif'):
        base_name = os.path.splitext(filename)[0]
        gt_text = f"This is the ground truth text for {base_name}"  
        gt_filename = f"{base_name}.gt.txt"
        
        # Write ground truth text to file
        with open(os.path.join(output_dir, gt_filename), 'w', encoding='utf-8') as f:
            f.write(gt_text)
