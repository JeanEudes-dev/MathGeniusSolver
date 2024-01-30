from sympy import symbols, sympify, diff, integrate

def perform_calculus_operations(expression):
    try:
        # Convert the input string to a sympy expression
        expr = sympify(expression)

        # Initialize symbols for symbolic calculations
        x = symbols('x')

        # Differentiate the expression
        derivative = diff(expr, x)

        # Integrate the expression
        integral = integrate(expr, x)

        # Create step-by-step explanations for each operation
        differentiation_steps = generate_differentiation_steps(expr)
        integration_steps = generate_integration_steps(expr)

        return {
            "derivative": derivative,
            "integral": integral,
            "explanation": {
                "differentiation": differentiation_steps,
                "integration": integration_steps
            }
        }

    except Exception as e:
        return None  # or handle the error as needed

def generate_differentiation_steps(expr):
    x = symbols('x')
    steps = []

    for _ in range(3):  # Generate three steps for differentiation
        expr = diff(expr, x)
        steps.append(str(expr))

    return steps

def generate_integration_steps(expr):
    x = symbols('x')
    steps = []

    for _ in range(3):  # Generate three steps for integration
        expr = integrate(expr, x)
        steps.append(str(expr))

    return steps
