from sympy import *
from sympy.abc import x, y

def gaussian_elim(__MatrixName__: str) -> str:
  return f'''
  pretty_print({__MatrixName__}.rref())
  '''

def gaussian_elim_parameters(__MatrixName__: str) -> str:
  return f'''pretty_print({__MatrixName__}.echelon_form())
Если Необходимо решить непростое уравнение в echelon_form - функция solve() поможет.


1) Исследуйте следующую систему уравнений на наличие "лишних" уравнений
pretty_print(solve({__MatrixName__}.det()))

2) Найдите количество решений следующей системы уравнений при различных значениях параметра
pretty_print(solve({__MatrixName__}.det())) <--- При этом параметре кол-во решений A.rank() - 1. В остальных случаях A.rank()
'''