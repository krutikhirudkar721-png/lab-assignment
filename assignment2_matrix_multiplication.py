# Multiply 5x3 and 3x2 matrices using user input and print result
import numpy as np

def get_matrix(rows, cols, name):
    print(f"\nEnter elements for {name} ({rows}x{cols}):")
    matrix = []

    for i in range(rows):
        row = list(map(int, input(f"Row {i+1}: ").split()))
        matrix.append(row)

    return np.array(matrix)

def multiply_matrices():
    # Input matrices
    A = get_matrix(5, 3, "Matrix A")
    B = get_matrix(3, 2, "Matrix B")

    print("\nMatrix A:\n", A)
    print("\nMatrix B:\n", B)

    # Multiply
    result = np.dot(A, B)

    print("\nProduct Matrix:\n", result)

if __name__ == "__main__":
    multiply_matrices()
