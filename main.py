import cv2
import numpy as np
import pytesseract


def preprocess_image(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresholded = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY_INV)
    contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:81]
    puzzle = np.zeros((9, 9), dtype=np.uint8)

    for i, contour in enumerate(contours):
        x, y, w, h = cv2.boundingRect(contour)
        digit_roi = thresholded[y:y+h, x:x+w]
        digit_text = pytesseract.image_to_string(digit_roi, config="--psm 10 --oem 3 -c tessedit_char_whitelist=123456789")
        if digit_text.isdigit():
            puzzle[i // 9][i % 9] = int(digit_text)

    return puzzle


def is_valid(puzzle, row, col, num):
    for i in range(9):
        if puzzle[row][i] == num or puzzle[i][col] == num:
            return False

    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if puzzle[start_row + i][start_col + j] == num:
                return False

    return True


def find_empty_location(puzzle):
    for row in range(9):
        for col in range(9):
            if puzzle[row][col] == 0:
                return row, col
    return None, None


def solve_sudoku(puzzle):
    row, col = find_empty_location(puzzle)
    if row is None or col is None:
        return True

    for num in range(1, 10):
        if is_valid(puzzle, row, col, num):
            puzzle[row][col] = num
            if solve_sudoku(puzzle):
                return True
            puzzle[row][col] = 0

    return False


# Preprocess the input image
image_path = "sudoku.png"  # Replace with your image path
sudoku_grid = preprocess_image(image_path)

# Solve the Sudoku puzzle
if solve_sudoku(sudoku_grid):
    print("Sudoku Solved:")
    for row in sudoku_grid:
        print(row)
else:
    print("No solution exists for the given Sudoku puzzle.")
