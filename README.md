# Numerical Analysis Project - Root Finding, System Solving, and PageRank Algorithm

This project consists of several numerical analysis exercises implemented in Python. It covers root-finding methods, solving linear systems of equations, and a PageRank-inspired algorithm for calculating the importance of pages within a network.

## Table of Contents
- [Project Overview](#project-overview)
- [Technologies Used](#technologies-used)
- [Installation and Setup](#installation-and-setup)
- [Features](#features)
- [How to Run](#how-to-run)
- [Additional Resources](#additional-resources)

## Project Overview
The project is divided into four main exercises:
1. **Root-Finding Methods**: Implements Bisection, Newton-Raphson, and Secant methods to approximate the roots of a given function.
2. **Modified Root-Finding Methods**: Adjusts the standard root-finding algorithms to increase precision and solve more complex root scenarios.
3. **Solving Linear Systems**: Uses LU decomposition to solve systems of equations in the form \(Ax = b\).
4. **PageRank-inspired Algorithm**: Calculates page importance based on adjacency matrices and applies the power method to approximate eigenvalues and eigenvectors.

For a detailed explanation of the mathematical methods and results, refer to the full [report (PDF in Greek)](./NumericalAnalysis.pdf).

## Technologies Used
- **Python**: The project was implemented and tested in Python using basic libraries and no external dependencies.
- **Markdown**: Used for documentation and project presentation on GitHub.

## Installation and Setup
1. Clone this repository:
    ```bash
    git clone https://github.com/theodougalis/Numerical-Analysis-Project---Root-Finding--System-Solving--and-PageRank-Algorithm.git
    ```
2. Make sure Python 3 is installed on your machine.
3. Navigate to the project directory and open the Python file `NumericalAnalysis.py` in your preferred Python environment.

## Features
### Exercise 1 - Root-Finding Methods
- **Bisection Method**: Approximates roots by iteratively narrowing down an interval.
- **Newton-Raphson Method**: Uses the derivative to converge quickly to a root.
- **Secant Method**: Similar to Newton-Raphson but does not require the derivative.

### Exercise 2 - Modified Root-Finding Methods
- Customized Bisection, Newton-Raphson, and Secant methods for enhanced accuracy and performance on complex root types.

### Exercise 3 - Solving Linear Systems with LU Decomposition
- Implements LU decomposition with pivoting to solve systems of linear equations.

### Exercise 4 - PageRank-inspired Algorithm for Page Importance
- Uses the power method to calculate page importance based on connectivity, inspired by Google's PageRank algorithm.
- Analyzes the effect of probability \(q\) on the importance of randomly accessing pages.

## How to Run
1. **Run Root-Finding Methods**:
   - To test the root-finding methods, execute:
     ```python
     python NumericalAnalysis.py
     ```
   - Use functions like `dixotomisif()`, `NRf()`, and `Secantf()` with appropriate parameters to find roots.

2. **Solve Linear Systems**:
   - To solve linear systems, use the function `axb()` for specific matrix and vector inputs.

3. **Calculate Page Importance**:
   - Run the `task1()` through `task6()` functions for different setups to simulate page importance under varying conditions.

## Additional Resources
- [Project Report (PDF)](./NumericalAnalysis.pdf) - Contains detailed explanations of the methods, calculations, and results in Greek.

---

