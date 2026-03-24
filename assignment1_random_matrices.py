import numpy as np

def random_matrices_operations():
    # Generate two 3x3 matrices with random integers (1 to 9)
    A = np.random.randint(1, 10, (3, 3))
    B = np.random.randint(1, 10, (3, 3))

    print("Matrix A:\n", A)
    print("\nMatrix B:\n", B)

    # Addition
    addition = A + B
    print("\nMatrix Addition:\n", addition)

    # Multiplication
    multiplication = np.dot(A, B)
    print("\nMatrix Multiplication:\n", multiplication)

if __name__ == "__main__":
    random_matrices_operations()
