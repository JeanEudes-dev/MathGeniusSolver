import numpy as np
from scipy.integrate import solve_ivp
from sympy import symbols, Function, dsolve, Eq

def solve_differential_equation(equation_str, initial_conditions, t_span):
    try:
        # Convert the input string to a sympy expression
        x, y = symbols('x y')
        equation = sympify(equation_str)

        # Define the function and the independent variable
        y_function = Function('y')(x)

        # Solve the differential equation using dsolve
        solution = dsolve(Eq(equation, 0), y_function)

        # Apply initial conditions
        for condition in initial_conditions:
            solution = solution.subs(y_function.diff(x, condition[0]), condition[1])

        # Extract the symbolic solution
        symbolic_solution = solution.rhs

        # If symbolic solution is successful, return it
        if symbolic_solution:
            return {"solution": symbolic_solution, "explanation": str(solution)}

        # If symbolic solution fails, try numerical solution using scipy
        def equation(t, y):
            return np.asarray([float(equation_str.replace('x', str(t)).replace('y', str(y[0])))])

        # Solve the differential equation using solve_ivp
        solution_scipy = solve_ivp(equation, t_span, initial_conditions)

        return {"solution": solution_scipy.y, "t_values": solution_scipy.t, "explanation": "Numerical solution using scipy"}

    except Exception as e:
        return None 
