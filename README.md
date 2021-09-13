# SudokuSolver
Python code to solver Sudoku puzzles as with different Constraint Satisfaction Problem (CSP) techniques

This program was made in my AI class to solve CSPs with different methods. The program has been modified to have a GUI (using pygame) and allows the user to easily try the 
different methods

The general strategy this program uses is a depth first search with backtracking. The user can choose different filtering or ordering options. 
Filtering filters out variable assignments that would break constraints, ordering helps decide whice variable to give an assignment next.

The filtering options are:
None- no filtering technique used
Forward checking - filter out new variable assignments that would lead to an immediate constraint violation
Arc consistency (AC3): AC3 filters out variable assignments that would lead to another variable having no valid assignments

The ordering options are:
Ordered: Solve the puzzle in order, column by column
Minimum remaining value (MRV): Pick the variable that has the smallest number of potential assignments in its domain.
Minimum remaining Value w/ Degree (MRVD): Same as MRV but break ties by degree (the number of other variables that share a constraint with a given variable, picking the highest)

NOTE: The sudokuGen file was not made by me and was given to the class to generate valid sudoku boards. Everything in the CSPSolver file is my own code
