# math_solver_backend/arithmetic/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ArithmeticHistory
from .arithmetic_solver import perform_arithmetic_calculations

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