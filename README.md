# Sudoku-Game
Sudoku Solver

This is a simple Sudoku solver implemented using Python and Pygame library. The solver uses a backtracking algorithm to find the solution for the given Sudoku puzzle.
Getting Started
Prerequisites

   . Python 3.11.6
   . Pygame library
   . sys library

Installation

To run the program, make sure you have Python and Pygame installed on your system. If you haven't installed Pygame, you can install it using pip:

bash

pip install pygame

Running the Program

To run the Sudoku solver, simply execute the Python script sudoku_solver.py:

bash

python sudoku_solver.py

Usage

    The Sudoku grid is provided as a 9x9 matrix in the grid variable in the code. You can modify this grid to solve different Sudoku puzzles.
    Left-click on the grid to input numbers manually. Numbers can be inputted from 1 to 9. Use the '0' key to erase a cell.
    Press the "Solve" button to automatically solve the Sudoku puzzle using the implemented algorithm.
    Press the "Reset" button to clear the entire Sudoku grid.
    Press the "Restart" button to reset the Sudoku grid to its initial state.

Controls

    Left-click: Input numbers into cells or interact with buttons.
    "Solve" button: Automatically solves the Sudoku puzzle.
    "Reset" button: Clears the entire Sudoku grid.
    "Restart" button: Resets the Sudoku grid to its initial state.

Implementation Details

    The solver uses a backtracking algorithm to find the solution for the Sudoku puzzle.
    The GUI is implemented using Pygame library.
    The program provides options to manually input numbers, solve the puzzle, reset the grid, and restart the game.

Acknowledgments

This code was written by [Mahmoud Ahmed and Mohammed Salma] for educational purposes. It's inspired by various Sudoku solving algorithms and Pygame tutorials available online. Feel free to use and modify this code for your own projects.
