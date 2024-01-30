from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import DifferentialEquationHistory
from .differential_equation_solver import solve_differential_equation

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
