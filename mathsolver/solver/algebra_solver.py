import re
from sympy import symbols, Eq, solve, sympify

def get_variables_from_expression(expression_data):
    # Collect all variables from the expression
    expression = sympify(expression_data)
    return expression.free_symbols

def solve_algebra_equation(expression_data):
    # Get variables from the expression
    variables = get_variables_from_expression(expression_data.replace("(",'').replace(')','').replace('=', '+'))
    print(variables)
    # Split the expression into individual equations based on non-alphanumeric characters
    equations_data = [eq.strip() for eq in re.split(r'[^a-zA-Z0-9_*]', expression_data) if eq]

    # Assume there is only one part if equations_data has length 1
    if len(equations_data) == 1:
        lhs, rhs = equations_data[0], '0'
    else:
        lhs, *rhs_list = equations_data
        rhs = "+".join(rhs_list)
        # print(lhs)
        # for i in range(len(rhs_list)):
        #     rhs_list[i] = f"{rhs_list[i]}"
        # rhs = "".join(rhs_list)
    
    # Rearrange the equation to isolate variables on one side
    equation = Eq(sympify(lhs) - sympify(rhs), 0)

    try:
        solution = solve(equation, variables)
        explanation = ""
        for sol in solution:
            explanation += f"Solutions for {', '.join(map(str, equation.free_symbols))}: {sol}, Expression Value: {sol.evalf()}\n"
    except Exception as e:
        solution = None
        explanation = f"Error in solving equation {equation}: {e}"

    if not solution:
        return {"result": None, "explanation": "The expression has no symbolic solution."}
    else:
        return {
            "result": str(solution[0]),  
            "explanation": explanation[:-1]
        }
