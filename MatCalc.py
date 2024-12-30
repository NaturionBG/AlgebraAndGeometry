from sympy import *
from sympy.abc import x, Y


def ComplexNumbers(index: int, MatrixName: str) -> str:
  return f'''
VarName1=x**{index} -1
VarName2=nroots(VarName1)
ListName1=[i for i in VarName2 if im(i)>0]
NumberName1=max(ListName1, key=lambda x: re(x))
MatrixName1={MatrixName}
VarName3=det(MatrixName1+NumberName1*eye(2))
print(re(VarName3))
print(im(VarName3))
'''