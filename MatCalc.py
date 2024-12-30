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


def Cartesian(Point1: str, Point2: str, Point3: str) -> str:
  return f'''
PointName1={Point1}
PointName2={Point2}
PointName3={Point3}
PointName4=Matrix([x, y])
LineName1=PointName3-PointName2
LineName2=PointName4-PointName1
VarName1, VarName2 = symbols('VarName1, VarName2')
__eqName1__=Eq(VarName1*PointName2[0] + VarName2, PointName2[1])
__eqName2__=Eq(VarName1*PointName3[0] + VarName2, PointName2[1])
solutionName1=solve([__eqName1__, __eqName2__])
__eqName3__=Eq(solutionName1[VarName1]*x + solutionName1[VarName2], y)
__eqName4__=Eq(LineName2.dot(LineName1), 0)
solutionName2=solve([__eqName3__, __eqName4__])
LineName2=LineName2.subs(solutionName2)
VarName3=(LineName2.dot(LineName2))**0.5
print(solutionName2[x].n())
print(solutionName2[y].n())
print(VarName3)
'''
