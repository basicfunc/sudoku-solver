import cv2
import numpy as np
import pytesseract


class SudokuSolver:
    def __init__(self, image_path):
        self.image_path = image_path
        self.puzzle = None

    def preprocess_image(self):
        image = cv2.imread(self.image_path)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        _, thresholded = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY_INV)
        contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contours = sorted(contours, key=cv2.contourArea, reverse=True)[:81]
        puzzle = np.zeros((9, 9), dtype=np.uint8)

        for i, contour in enumerate(contours):
            x, y, w, h = cv2.boundingRect(contour)
            digit_roi = thresholded[y:y + h, x:x + w]
            digit_text = pytesseract.image_to_string(digit_roi, config="--psm 10 --oem 3 -c tessedit_char_whitelist=123456789")
            if digit_text.isdigit():
                puzzle[i // 9][i % 9] = int(digit_text)

        self.puzzle = puzzle

    def is_valid(self, row, col, num):
        for i in range(9):
            if self.puzzle[row][i] == num or self.puzzle[i][col] == num:
                return False

        start_row = (row // 3) * 3
        start_col = (col // 3) * 3
        for i in range(3):
            for j in range(3):
                if self.puzzle[start_row + i][start_col + j] == num:
                    return False

        return True

    def find_empty_location(self):
        for row in range(9):
            for col in range(9):
                if self.puzzle[row][col] == 0:
                    return row, col
        return None, None

    def solve_sudoku(self):
        row, col = self.find_empty_location()
        if row is None or col is None:
            return True

        for num in range(1, 10):
            if self.is_valid(row, col, num):
                self.puzzle[row][col] = num
                if self.solve_sudoku():
                    return True
                self.puzzle[row][col] = 0

        return False

    def solve(self):
        self.preprocess_image()
        if self.puzzle is None:
            return None

        if self.solve_sudoku():
            return self.puzzle
        else:
            return None


def print_solution(puzzle):
    if puzzle is None:
        print("No solution exists for the given Sudoku puzzle.")
        return

    print("Sudoku Solved:")
    for row in puzzle:
        print(row)


if __name__ == '__main__':    
    # Create SudokuSolver instance and solve
    image_path = "sudoku.png"  # Replace with your image path
    solver = SudokuSolver(image_path)
    solution = solver.solve()

    # Print the solution
    print_solution(solution)
