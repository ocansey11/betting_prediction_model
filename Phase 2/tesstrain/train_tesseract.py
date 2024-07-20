import os
import subprocess

# Directories
ground_truth_dir = 'data\\eng\\ground-truth'
output_dir = 'data\\eng\\output'
os.makedirs(output_dir, exist_ok=True)

# Tesseract path
tesseract_path = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Train command template
train_command = [
    tesseract_path,
    '',  # Placeholder for input image path
    '',  # Placeholder for output base path
    '--psm', '6',
    'lstm.train'
]

# Run the command for each image in the ground truth directory
for filename in os.listdir(ground_truth_dir):
    if filename.endswith('.png'):
        image_path = os.path.join(ground_truth_dir, filename)
        output_path = os.path.join(output_dir, os.path.splitext(filename)[0])
        train_command[1] = image_path
        train_command[2] = output_path
        subprocess.run(train_command)

# Combine generated lstmf files
subprocess.run(['combine_tessdata', output_dir])

# Create the final trained model
lstmtraining_command = [
    'lstmtraining',
    '--continue_from', 'data\\eng.lstm',
    '--model_output', 'data\\eng.traineddata',
    '--traineddata', 'data\\eng\\eng.traineddata',
    '--train_listfile', 'data\\eng\\output\\all-lstmf'
]
subprocess.run(lstmtraining_command)
