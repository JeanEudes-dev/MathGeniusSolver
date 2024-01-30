from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CalculusHistory
from .calculus_solver import perform_calculus_operations

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
