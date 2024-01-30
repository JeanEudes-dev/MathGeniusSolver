from django.urls import path
from .views import AlgebraSolver, TrigonometrySolver, ArithmeticSolver, LinearAlgebraSolver, CalculusSolver, DifferentialEquationSolver

urlpatterns = [
    path('solve/trigonometry/', TrigonometrySolver.as_view(), name='Trigonometry-solver'),
    path('solve/algebra/', AlgebraSolver.as_view(), name='Algebra-solver'),
    path('solve/arithmetic/',  ArithmeticSolver.as_view(), name="Arithmetic-solver"),
    path('solve/linear-algebra/', LinearAlgebraSolver.as_view(), name='Linear-algebra-solver'),
    path('solve/calculus/',  CalculusSolver.as_view(), name='calculus-solver'),
    path('solve/differential/', DifferentialEquationSolver.as_view(), name='differential-solver')
]