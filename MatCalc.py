from sympy import *
from sympy.abc import x, y

def EigenValsAndVects(MatrixName:str) -> str:
  return f'''
__MatrixName1__={MatrixName}
NumberName1=max(list(__MatrixName1__.eigenvals().keys()), key=lambda x: im(x)).n()
VectorName=Matrix([1, x, y])
EndMatrixName=(__MatrixName1__-NumberName1*eye(3))*VectorName
solutionName=solve([EndMatrixName[0], EndMatrixName[1]])
print(im(Z))
print(re(solutionName[x]))
'''

