import numpy as np
from sympy import symbols, sin, cos, tan, asin, acos, atan, simplify, rad

def solve_trigonometry(input_data):
    try:
        if 'operation' in input_data:
            # Single trigonometric operation
            operation = input_data['operation']
            angle_value = input_data.get('angle_value')

            # Convert angle to radians
            angle_rad = rad(angle_value)

            if operation == "sine":
                result = np.sin(angle_rad)
                explanation = f"Calculating sine of {angle_value} degrees."

            elif operation == "cosine":
                result = np.cos(angle_rad)
                explanation = f"Calculating cosine of {angle_value} degrees."

            elif operation == "tangent":
                result = np.tan(angle_rad)
                explanation = f"Calculating tangent of {angle_value} degrees."

            elif operation == "arcsine":
                result = np.degrees(asin(angle_value))
                explanation = f"Calculating arcsine of {angle_value}."

            elif operation == "arccosine":
                result = np.degrees(acos(angle_value))
                explanation = f"Calculating arccosine of {angle_value}."

            elif operation == "arctangent":
                result = np.degrees(atan(angle_value))
                explanation = f"Calculating arctangent of {angle_value}."

            else:
                raise ValueError("Invalid trigonometry operation")

            return {"result": result, "explanation": explanation}

        elif 'expression' in input_data:
            # Composed trigonometric expression
            expression = input_data['expression']

            # Define symbolic variable
            x = symbols('x')

            # Convert angle to radians if it contains degrees
            expression = expression.replace("sin(", "sin(rad(").replace("cos(", "cos(rad(").replace("tan(", "tan(rad(")

            # Parse and simplify the expression
            parsed_expression = simplify(expression)

            # Evaluate the expression numerically
            result = float(parsed_expression.evalf(subs={x: 1}))

            explanation = f"Solving the trigonometric expression: {expression}"

            return {"result": result, "explanation": explanation}

        else:
            raise ValueError("Invalid input data for trigonometry solver")

    except Exception as e:
        return None  # or handle the error as needed
