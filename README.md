# Sudoku Solver

The Sudoku Solver is a Python script that takes an image containing a Sudoku puzzle as input and solves it using the backtracking algorithm. It utilizes OpenCV for image processing, NumPy for array manipulation, and Tesseract OCR for digit recognition.

## Prerequisites

To run the Sudoku Solver script, you need to have the following dependencies installed:

- Python 3.x
- OpenCV (cv2)
- NumPy
- pytesseract

You can install these dependencies using pip by running the following command:

```
pip install opencv-python numpy pytesseract
```

Additionally, you need to have Tesseract OCR installed on your system. You can download and install Tesseract from the official GitHub repository: [https://github.com/tesseract-ocr/tesseract](https://github.com/tesseract-ocr/tesseract).

## Usage

To use the Sudoku Solver script, follow these steps:

1. Make sure you have the Sudoku puzzle image ready. The image should contain a clear and well-defined Sudoku puzzle.

2. Place the Sudoku puzzle image in the same directory as the script file, or provide the full path to the image in the `image_path` variable in the script.

3. Run the script using the command: `python sudoku_solver.py`

4. The script will preprocess the image, extract the puzzle, solve it, and display the solution if found. The solution will be printed in a human-readable format.

Note: The script assumes that the Sudoku puzzle in the image is a standard 9x9 grid. If the puzzle size or format is different, the script may not work correctly.

## Customization

If you want to customize or modify the script, you can make changes to the following sections:

- **Image Preprocessing**: The `preprocess_image()` method contains the image preprocessing steps such as loading the image, converting it to grayscale, thresholding, and contour extraction. You can modify these steps based on your specific image requirements.

- **OCR Configuration**: The Tesseract OCR configuration used for digit recognition can be modified in the `image_to_string()` function call. You can experiment with different configurations to improve digit recognition accuracy.

- **Output Format**: The `print_solution()` function prints the solved puzzle in a human-readable format. You can modify this function to change the output format or display the solution in a different way.

## Limitations

The Sudoku Solver script has a few limitations:

- The accuracy of digit recognition depends on the quality and clarity of the input image. Noisy or poorly defined images may result in incorrect digit recognition and consequently an incorrect solution.

- The script assumes that the Sudoku puzzle in the image is a standard 9x9 grid. If the puzzle size or format is different, the script may not work correctly.

- In some cases, the script may not be able to find a solution for certain Sudoku puzzles, even if they are valid. This can happen if the puzzle has multiple valid solutions or if the backtracking algorithm fails to find a solution within a reasonable amount of time.

## License

This Sudoku Solver script is released under the [MIT License](https://opensource.org/licenses/MIT). Feel free to modify and distribute it according to your needs.

## Acknowledgements

The script was created using various libraries and resources, including:

- [OpenCV](https://opencv.org/): An open-source computer vision and machine learning library.
- [NumPy](https://numpy.org/): A fundamental package for scientific computing with Python.
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract): An open-source OCR engine.

Special thanks to the contributors of these projects for their valuable work.

## Disclaimer

The Sudoku Solver script is provided as-is without any guarantee or warranty. Use it at your own risk. The script may not always produce accurate solutions, and the author is not responsible for any incorrect results or damages caused by the use of this script.
