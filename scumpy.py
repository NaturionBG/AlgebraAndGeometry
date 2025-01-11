from sympy import *
from sympy.abc import x, y

def gaussian_elim(num:int, __MatrixName__: str) -> str:
  return [f'''
  pretty_print({__MatrixName__}.rref())
  '''][num-1]

def gaussian_elim_parameters(num:int, __MatrixName__: str) -> str:
  return [f'''pretty_print({__MatrixName__}.echelon_form())
Если Необходимо решить непростое уравнение в echelon_form - функция solve() поможет.
'''][num-1]