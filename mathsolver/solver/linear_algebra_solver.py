import numpy as np
from scipy.linalg import solve, eig, svd, lu

def solve_linear_algebra_problem(problem_type, matrix_data):
    try:
        if problem_type == "system_of_equations":
            # Solve a system of linear equations
            coefficients = matrix_data['coefficients']
            constants = matrix_data['constants']
            solution = solve(coefficients, constants)
            explanation = f"Solving the system of linear equations:\n{coefficients} * X = {constants}"

        elif problem_type == "eigenvalues_eigenvectors":
            # Find eigenvalues and eigenvectors
            matrix = matrix_data['matrix']
            eigenvalues, eigenvectors = eig(matrix)
            explanation = f"Finding eigenvalues and eigenvectors of the matrix:\n{matrix}"

            # Format the results for easier interpretation
            eigenvalues = eigenvalues.tolist()
            eigenvectors = eigenvectors.tolist()

            solution = {"eigenvalues": eigenvalues, "eigenvectors": eigenvectors}

        elif problem_type == "singular_value_decomposition":
            # Perform Singular Value Decomposition (SVD)
            matrix = matrix_data['matrix']
            u, s, vt = svd(matrix)
            explanation = f"Performing Singular Value Decomposition (SVD) of the matrix:\n{matrix}"

            # Format the results for easier interpretation
            u = u.tolist()
            s = s.tolist()
            vt = vt.tolist()

            solution = {"U": u, "S": s, "Vt": vt}

        elif problem_type == "matrix_factorization":
            # Perform LU matrix factorization
            matrix = matrix_data['matrix']
            p, l, u = lu(matrix)
            explanation = f"Performing LU matrix factorization of the matrix:\n{matrix}"

            # Format the results for easier interpretation
            p = p.tolist()
            l = l.tolist()
            u = u.tolist()

            solution = {"P": p, "L": l, "U": u}

        elif problem_type == "matrix_operations":
            # Perform basic matrix operations (e.g., addition, multiplication)
            matrix_a = matrix_data['matrix_a']
            matrix_b = matrix_data['matrix_b']
            operation = matrix_data['operation']
            
            if operation == "addition":
                result = np.add(matrix_a, matrix_b)
            elif operation == "multiplication":
                result = np.dot(matrix_a, matrix_b)

            explanation = f"Performing {operation} of matrices:\nMatrix A:\n{matrix_a}\nMatrix B:\n{matrix_b}"

            solution = {"result": result}

        else:
            raise ValueError("Invalid linear algebra problem type")

        return {"solution": solution, "explanation": explanation}

    except Exception as e:
        return None  # or handle the error as needed