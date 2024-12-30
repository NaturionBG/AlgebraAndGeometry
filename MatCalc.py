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


def Polynomials(pol: any) -> str:
  return f'''
VarName1={pol}
VarName2=nroots(VarName1)
ListName1=[abs(i) for i in VarName2]
NumberName1=max(VarName2, key=lambda x: re(x))
print(sum(ListName1))
print(re(NumberName1))
'''