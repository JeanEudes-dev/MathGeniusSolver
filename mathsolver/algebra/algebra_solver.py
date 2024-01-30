from sympy import symbols, sympify, solve, Eq

def perform_algebraic_calculations(expression):
    try:
        # Convert the input string to a sympy expression
        expr = sympify(expression)
        
        # Solve the expression symbolically
        solution = solve(expr)

        # Check if the solution is numeric or symbolic
        if all(isinstance(sol, (int, float)) for sol in solution):
            return {"result": solution, "explanation": "Numeric solution"}
        else:
            # If symbolic, provide a step-by-step solution
            explanation = []
            for sol in solution:
                # Create an equation to explain each step
                equation = Eq(expr, sol)
                explanation.append(f"Solving {equation}")

            return {"result": solution, "explanation": explanation}

    except Exception as e:
        return None
