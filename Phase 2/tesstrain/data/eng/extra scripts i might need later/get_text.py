import os
import subprocess

# Directories
input_dir = './images'
output_dir = './tesseract_outputs'
post_cleaned_dir = './post_cleaned_outputs'

# Create output directories if they don't exist
os.makedirs(output_dir, exist_ok=True)
os.makedirs(post_cleaned_dir, exist_ok=True)

# Iterate over all files in the input directory
for filename in os.listdir(input_dir):
    if filename.endswith('.png'):  # Modify this line if you have other image formats
        input_path = os.path.join(input_dir, filename)
        base_name = os.path.splitext(filename)[0]
        output_path = os.path.join(output_dir, base_name)

        # Run Tesseract to get text
        subprocess.run(['tesseract', input_path, output_path, '-l', 'eng', '--psm', '6'])

        # Read the extracted text for post-cleaning
        text_path = output_path + '.txt'
        post_cleaned_text_path = os.path.join(post_cleaned_dir, base_name + '.txt')
        
        with open(text_path, 'r') as f:
            text_content = f.read()

        # Post-cleaning function (you can modify this to fit your needs)
        def post_clean(text_content):
            # Example post-cleaning: simple text transformation
            cleaned_content = text_content.replace(' ', '\t')  # Example: replace spaces with tabs
            return cleaned_content

        cleaned_content = post_clean(text_content)
        
        # Save the post-cleaned content
        with open(post_cleaned_text_path, 'w') as f:
            f.write(cleaned_content)

print("Processing complete.")
