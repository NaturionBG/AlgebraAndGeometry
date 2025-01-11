from sympy import *
from sympy.abc import x, Y


def ComplexNumbers(num:int, index: int, MatrixName: Matrix) -> str:
  return [f'''
# Первое решение \n  

VarName1=x**{index} -1
VarName2=nroots(VarName1)
ListName1=[i for i in VarName2 if im(i)>0]
NumberName1=max(ListName1, key=lambda x: re(x))
MatrixName1={MatrixName}
VarName3=det(MatrixName1+NumberName1*eye(2))
print(re(VarName3))
print(im(VarName3))
''',
f'''
# Второе решение \n

from math import cos, sin, pi
stepen_kornya = {index}
roots = []
lambdich = []
maxcosinus = 0
A = {MatrixName}
for i in range(stepen_kornya):
    cosinus = cos(2 * i * pi / stepen_kornya)
    sinus = sin(2 * i * pi / stepen_kornya)
    if sinus > 0 and cosinus > maxcosinus:
        maxcosinus = cosinus
        lambdich = [cosinus, sinus]
lambda_matrix = eye(2)
lambda_matrix *= complex(lambdich[0], lambdich[1])
print(round((lambda_matrix + A).det(), 3))
'''][num-1]


def Polynomials(num:int, pol: any) -> str:
  return [f'''
VarName1={pol}
VarName2=nroots(VarName1)
ListName1=[abs(i) for i in VarName2]
NumberName1=max(VarName2, key=lambda x: re(x))
print(sum(ListName1))
print(re(NumberName1))
'''][num-1]