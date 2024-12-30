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
  
def MatrixEquations(name1: str, name2: str, name3: str = None) -> str:
  if name3!=None:
    return f'''pretty_print({name1}.inv()*{name3}*({name2}.inv()))'''
  else:
    return f'''Если у вас вид: AX=B, то код: pretty_print({name1}.inv()*{name2})
    Если же вид: XA=B, то код: pretty_print({name2}*({name1}.inv()))'''
    
def Deter(name1: str, name2: str = None) -> str:
  if name2!=None:
    return f'''name3={name1}*{name2}
    __equationName__ = Eq(det(name3), 0)
    VarName=solve(__equationName__)
    В оформлении задания на бумаге самостоятельно найдите, линейной комбинацией 
    каких строк/столбцов является столбец/строка с параметром'''
  else:
    return f'''pretty_print(det({name1}))
    В оформлении задания на бумаге распишите, как вы находили определитель.'''
    
    