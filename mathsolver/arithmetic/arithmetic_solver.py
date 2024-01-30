from sympy import symbols, sympify, solve, Eq

def perform_arithmetic_calculations(expression):
    try:
        # Split the expression into individual steps
        steps = expression.split(';')

        # Initialize symbols for symbolic calculations
        x, y, z = symbols('x y z')

        # Initialize the result
        result = 0

        # Initialize the explanation
        explanation = []

        # Perform each step
        for step in steps:
            # Convert the step string to a sympy expression
            expr = sympify(step)

            # Check if the expression contains variables
            if any(var in expr.free_symbols for var in (x, y, z)):
                # If it contains variables, solve symbolically
                solution = solve(expr)

                # Create an explanation for each step
                explanation.append(f"Solving {Eq(expr, solution)}")

                # Update the result with the symbolic solution
                result = solution

            else:
                # If no variables, evaluate numerically
                result = eval(step)

                # Create an explanation for each step
                explanation.append(f"Step: {step} = {result}")

        return {"result": result, "explanation": explanation}

    except Exception as e:
        # Return an error message if anything goes wrong
        print(f'error: str(e)')
        return None
    