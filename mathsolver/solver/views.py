from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .algebra_solver import  solve_algebra_equation
from .arithmetic_solver import perform_arithmetic_calculations
from .linear_algebra_solver import solve_linear_algebra_problem
from .trygonometry_solver import solve_trigonometry
from .differential_equation_solver import solve_differential_equation
from .calculus_solver import perform_calculus_operations

class AlgebraSolver(APIView):
    def post(self, request):
        # Retrieve data from request.data
        expression = request.data.get('expression')
        expression = 'x**2+5=0'
        # Perform algebraic calculations using the external function
        result = solve_algebra_equation(expression)

        if result is None:
            return Response({'error': 'Invalid expression Please check your Expression and try again'}, status=status.HTTP_400_BAD_REQUEST)

        # Save to the database
        algebra_history = AlgebraHistory.objects.create(
            expression=expression,
            result=result['result']
        )

        return Response({'result': result['result'], 'explanation': result['explanation'], 'history_id': algebra_history.id}, status=status.HTTP_200_OK)
    


class ArithmeticSolver(APIView):
    def post(self, request):
        # Retrieve data from request.data
        expression = request.data.get('expression')

        # Perform arithmetic calculations using the external function
        result = perform_arithmetic_calculations(expression)

        if result is None:
            return Response({'error': 'Invalid expression'}, status=status.HTTP_400_BAD_REQUEST)

        # Save to the database
        arithmetic_history = ArithmeticHistory.objects.create(
            expression=expression,
            result=result['result']
        )

        return Response({'result': result['result'], 'explanation': result['explanation'], 'history_id': arithmetic_history.id}, status=status.HTTP_200_OK)



class LinearAlgebraSolver(APIView):
    def post(self, request):
        # Retrieve data from request.data
        problem_type = request.data.get('problem_type')
        matrix_data = request.data.get('matrix_data')

        # Perform linear algebra problem solving using the external function
        result = solve_linear_algebra_problem(problem_type, matrix_data)

        if result is None:
            return Response({'error': 'Invalid linear algebra problem or parameters'}, status=status.HTTP_400_BAD_REQUEST)

        # Save to the database
        linear_algebra_history = LinearAlgebraHistory.objects.create(
            problem_type=problem_type,
            solution=result['solution']
        )

        return Response({'solution': result['solution'], 'explanation': result['explanation'], 'history_id': linear_algebra_history.id}, status=status.HTTP_200_OK) 

class CalculusSolver(APIView):
    def post(self, request):
        # Retrieve data from request.data
        expression = request.data.get('expression')

        # Perform calculus operations using the external function
        result = perform_calculus_operations(expression)

        if result is None:
            return Response({'error': 'Invalid expression'}, status=status.HTTP_400_BAD_REQUEST)

        # Save to the database
        calculus_history = CalculusHistory.objects.create(
            expression=expression,
            derivative=result['derivative'],
            integral=result['integral']
        )

        return Response({'derivative': result['derivative'], 'integral': result['integral'], 'explanation': result['explanation'], 'history_id': calculus_history.id}, status=status.HTTP_200_OK)

class DifferentialEquationSolver(APIView):
    def post(self, request):
        # Retrieve data from request.data
        equation_str = request.data.get('equation')
        initial_conditions = request.data.get('initial_conditions', [])
        t_span = request.data.get('t_span', [0, 10])

        # Perform differential equation solving using the external function
        result = solve_differential_equation(equation_str, initial_conditions, t_span)

        if result is None:
            return Response({'error': 'Invalid equation or parameters'}, status=status.HTTP_400_BAD_REQUEST)

        # Save to the database
        differential_equation_history = DifferentialEquationHistory.objects.create(
            equation=equation_str,
            solution=result['solution']
        )

        return Response({'solution': result['solution'].tolist(), 't_values': result['t_values'].tolist(), 'explanation': result['explanation'], 'history_id': differential_equation_history.id}, status=status.HTTP_200_OK)


class TrigonometrySolver(APIView):
    def post(self, request):
        # Retrieve data from request.data
        input_data = request.data

        # Perform trigonometry solving using the external function
        result = solve_trigonometry(input_data)

        if result is None:
            return Response({'error': 'Invalid trigonometry input or parameters'}, status=status.HTTP_400_BAD_REQUEST)

        # Save to the database
        trigonometry_history = TrigonometryHistory.objects.create(
            result=result['result'],
            explanation=result['explanation']
        )

        return Response({'result': result['result'], 'explanation': result['explanation'], 'history_id': trigonometry_history.id}, status=status.HTTP_200_OK)
