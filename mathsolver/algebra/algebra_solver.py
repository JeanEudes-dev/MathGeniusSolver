def perform_algebraic_calculations(expression):
    try:
        result = eval(expression)
        return result
    except Exception as e:
        return None