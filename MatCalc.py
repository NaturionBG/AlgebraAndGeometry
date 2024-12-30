from sympy import *
from sympy.abc import x, y

def gaussian_elim() -> str:
  return f'pretty_print(__MatrixName__.rref())'

def gaussian_elim_parameters() -> str:
  return '''pretty_print(__MatrixName__.echelon_form())
Если Необходимо решить непростое уравнение в echelon_form - функция solve() поможет.'''