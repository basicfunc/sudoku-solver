import cv2
import numpy as np
import pytesseract

class SudokuSolver:
    # Constructor to initialize a new instance of the class with an image path and a puzzle attribute.
    def __init__(self, image_path):
        self.image_path = image_path
        self.puzzle = None

    # Method to load the image at the specified path, converts it to grayscale, thresholds it to create a binary image,
    # finds the contours in the image, and extracts the digits from the image using Tesseract OCR. 
    # The extracted digits are stored in a NumPy array representing the Sudoku puzzle.
    def preprocess_image(self):
        # Load the image and convert it to grayscale
        image = cv2.imread(self.image_path)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # Threshold the image to create a binary image
        _, thresholded = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY_INV)
        
        # Find contours in the image and sort them by area
        contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contours = sorted(contours, key=cv2.contourArea, reverse=True)[:81]
        
        # Extract digits from the image and store them in a NumPy array
        puzzle = np.zeros((9, 9), dtype=np.uint8)
        for i, contour in enumerate(contours):
            x, y, w, h = cv2.boundingRect(contour)
            digit_roi = thresholded[y:y + h, x:x + w]
            
            # Use Tesseract OCR to recognize the digit in the ROI
            digit_text = pytesseract.image_to_string(digit_roi, config="--psm 10 --oem 3 -c tessedit_char_whitelist=123456789")
            if digit_text.isdigit():
                puzzle[i // 9][i % 9] = int(digit_text)
        
        self.puzzle = puzzle

    # Method to check if a given number is valid in a given row, column, or 3x3 subgrid of the Sudoku puzzle.
    def is_valid(self, row, col, num):
        # Check if the given number is valid in the given row and column
        for i in range(9):
            if self.puzzle[row][i] == num or self.puzzle[i][col] == num:
                return False
        
        # Check if the given number is valid in the 3x3 subgrid
        start_row = (row // 3) * 3
        start_col = (col // 3) * 3
        for i in range(3):
            for j in range(3):
                if self.puzzle[start_row + i][start_col + j] == num:
                    return False
        
        return True

    # Method to find the first empty cell in the Sudoku puzzle.
    def find_empty_location(self):
        # Find the first empty cell in the puzzle
        for row in range(9):
            for col in range(9):
                if self.puzzle[row][col] == 0:
                    return row, col
        return None, None

    # Method to solve the Sudoku puzzle, uses backtracking and recursion.
    def solve_sudoku(self):
        # Find an empty cell in the puzzle
        row, col = self.find_empty_location()
        if row is None or col is None:
            # If there are no empty cells left, the puzzle is solved
            return True
        
        # Try each number from 1 to 9 in the empty cell
        for num in range(1, 10):
            if self.is_valid(row, col, num):
                # If the number is valid, place it in the cell and recurse
                self.puzzle[row][col] = num
                if self.solve_sudoku():
                    return True
                # If the recursion did not solve the puzzle, backtrack
                self.puzzle[row][col] = 0
        
        return False

    # Extract the Sudoku puzzle from the input image, and then solve the puzzle
    def solve(self):
        # Preprocess the input image and extract the puzzle
        self.preprocess_image()
        if self.puzzle is None:
            # If no puzzle was found in the image, return None
            return None
        
        # Solve the puzzle and return the solution
        if self.solve_sudoku():
            return self.puzzle
        else:
            # If no solution was found, return None
            return None

# Prints it in a human-readable format.
def print_solution(puzzle):
    # Print the solved puzzle in a human-readable format
    if puzzle is None:
        print("No solution exists for the given Sudoku puzzle.")
        return
    
    print("Sudoku Solved:")
    for row in puzzle:
        print(row)

if __name__ == '__main__':
    # Create a SudokuSolver instance and solve the puzzle in the input image
    image_path = "sudoku.png" # Replace with your image path
    solver = SudokuSolver(image_path)
    solution = solver.solve()
    
    # Print the solution
    print_solution(solution)
