from sympy import symbols, sympify, solve, Eq, sqrt, latex
import re

def preprocess_expression(expression):
    # Replace LaTeX-style fractions like \frac{a}{b} with sympy.Rational() syntax
    expression = re.sub(r'\\frac{(\d+)}{(\d+)}', r'sympy.Rational(\1, \2)', expression)
    return expression


def latex_to_sympy(latex_expression):
    # Convert LaTeX expression to Sympy expression
    return sympify(latex_expression)

def perform_algebraic_calculations(latex_expression):
    try:
        # Convert LaTeX expression to Sympy expression
        expr = latex_to_sympy(latex_expression)

        # Check if the expression is an equation
        if isinstance(expr, Eq):
            solution = solve(expr, dict=True)
            explanation = f"Solving the equation {latex(expr)}:\n"

            for sol in solution:
                explanation += f"Solution: {sol}\n"

            return {"result": solution, "explanation": explanation[:-1]}

        # Solve the expression symbolically
        solution = solve(expr)
        
        if not solution:
            return {"result": latex(expr), "explanation": "Numeric solution"}
        else:
            explanation = ""
            
            for sol in solution:
                explanation += f"Solution: {sol}, Expression Value: {sol.evalf()}\n"
                
            return {"result": latex(solution[0]),  
                    "explanation": explanation[:-1]}
    
    except Exception as e:
        print(f"error: {str(e)}")
        return None

# Testing code
if __name__ == '__main__':
    print(perform_algebraic_calculations("x^2 + 3*x - 4"))
    print(perform_algebraic_calculations("x=4+-4"))
    print(perform_algebraic_calculations("sqrt(5)*sin(pi/5)"))
    print(perform_algebraic_calculations("\\frac{7}{9}"))
    print(perform_algebraic_calculations("\\frac{32}{6}"))
