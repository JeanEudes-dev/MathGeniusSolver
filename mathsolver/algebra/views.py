from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import AlgebraHistory
from .algebra_solver import perform_algebraic_calculations

class AlgebraSolver(APIView):
    def post(self, request):
        # Retrieve data from request.data
        expression = request.data.get('expression')

        # Perform algebraic calculations using the external function
        result = perform_algebraic_calculations(expression)

        if result is None:
            return Response({'error': 'Invalid expression'}, status=status.HTTP_400_BAD_REQUEST)

        # Save to the database
        algebra_history = AlgebraHistory.objects.create(
            expression=expression,
            result=result['result']
        )

        return Response({'result': result['result'], 'explanation': result['explanation'], 'history_id': algebra_history.id}, status=status.HTTP_200_OK)