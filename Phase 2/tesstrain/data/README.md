# Tesseract Training Data for English Language

This directory contains the ground truth data and outputs necessary for training Tesseract OCR to recognize custom symbols.

## Directory Structure

- `ground-truth/`: Contains the training images, their corresponding text files, and box files.
- `output/`: This will contain the output files generated during the training process.

## Contents

### ground-truth/

This directory contains:

- `image3.png`: Example training image.
- `image3.gt.txt`: Ground truth text file corresponding to `image3.png`.
- `image3.box`: Box file corresponding to `image3.png`.

Each ground truth file should have the same base name as the image it corresponds to, with the appropriate extension.

### output/

This directory will be populated with intermediate and final output files during the training process. Make sure it is empty before starting the training process.

## Training Process

To start the training process, follow these steps:

1. Ensure all training images, ground truth text files, and box files are placed in the `ground-truth/` directory.
2. Run the `train.bat` file located in the root of the `tesstrain` directory.
3. The `output/` directory will be populated with training artifacts, including the final trained data.

## Notes

- Make sure that the text in the ground truth files accurately represents the text in the images, including any custom symbols.
- Ensure that the box files correctly define the bounding boxes for each character or symbol in the images.
- You can use `jTessBoxEditor` to create and edit box files if necessary. You can find this in `Phase2/tools`

## After Training

- Run `tesseract path\to\data\eng\test_images\<image.png> <path\to\output> -l eng`

For more details on the training process, refer to the Tesseract documentation and the `README.md` in the root of the `tesstrain` repository.

---

Happy training!
