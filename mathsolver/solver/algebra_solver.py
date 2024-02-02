from sympy import symbols, Eq, solve, sympify
import re  # Import the 're' module for regular expressions

def get_variables_from_expression(expression_data):
    # Collect all variables from the expression
    expression = sympify(expression_data)
    return expression.free_symbols

def solve_algebra_equation(expression_data):
    # Get variables from the expression
    variables = get_variables_from_expression(expression_data.replace('=', ''))

    # Split the expression into individual equations based on non-alphanumeric characters
    equations_data = [eq.strip() for eq in re.split(r'[^a-zA-Z0-9_*]', expression_data) if eq]

    # Assume there is only one part if equations_data has length 1
    if len(equations_data) == 1:
        lhs, rhs = equations_data[0], '0'
    else:
        lhs, *rhs_list = equations_data
        rhs = '+'.join(rhs_list)

    # Rearrange the equation to isolate variables on one side
    equation = Eq(sympify(lhs) - sympify(rhs), 0)

    try:
        solution = solve(equation, variables)
        explanation = f"Solutions for {', '.join(map(str, equation.free_symbols))}: {solution}"
    except Exception as e:
        solution = None
        explanation = f"Error in solving equation {equation}: {e}"

    if not solution:
        return {"result": None, "explanation": "The expression has no symbolic solution."}
    else:
        explanation = ""
        for sol in solution:
            explanation += f"Solution: {sol}, Expression Value: {sol.evalf()}\n"
                
        return {
                "result": solution[0],  
                # "result": latex(solution[0]),  
                "explanation": explanation[:-1]
            }
