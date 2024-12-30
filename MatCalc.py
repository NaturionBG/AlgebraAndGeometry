from sympy import *
from sympy.abc import x, Y

def gaussian_elim_3vars(__MatrixName__: Matrix) -> str:
  return f'pretty_print({__MatrixName__}.rref())'

