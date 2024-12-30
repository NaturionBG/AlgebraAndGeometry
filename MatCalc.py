from sympy import *
from sympy.abc import x, Y

def MatrixOps(__MatrixName1__: str, __MatrixName2__: str, OPS: list[str]) -> str:
  if 'kron' in OPS:
    return f'''__ResultName1__ = {__MatrixName1__}*transpose({__MatrixName2__})
  __ResultName2__ = transpose({__MatrixName1__})*{__MatrixName2__}
  __ResultName3__ = kronecker_product(__ResultName1__, __ResultName2__)
  print(trace(__ResultName1__))
  print(trace(__ResultName3__))'''
  else:
    return f'''__ResultName1__ = {__MatrixName1__}*transpose({__MatrixName2__})
  __ResultName2__ = transpose({__MatrixName1__})*{__MatrixName2__}
  print(max(__ResultName1__))
  print(sum(__ResultName2__))'''
  
