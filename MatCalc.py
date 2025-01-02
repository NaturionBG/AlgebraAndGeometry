from sympy import *
from sympy.abc import x, y

def EigenValsAndVects(MatrixName:str) -> str:
  return f'''
# Первое решение:\n
  
__MatrixName1__={MatrixName}
NumberName1=max(list(__MatrixName1__.eigenvals().keys()), key=lambda x: im(x)).n()
VectorName=Matrix([1, x, y])
EndMatrixName=(__MatrixName1__-NumberName1*eye(3))*VectorName
solutionName=solve([EndMatrixName[0], EndMatrixName[1]])
print(im(Z))
print(re(solutionName[x]))

# Второе решение:\n

A = {MatrixName}
lambda_values = A.charpoly()

Z = max(solve(lambda_values.args[0]), key=lambda x: im(x))

B = A - (Z * eye(3))
own_vector = [i.n() for i in B.nullspace()[0]]
need_to_mul = solve(own_vector[0] * x - 1, (x))[0]
new_vector_values = [simplify(i * need_to_mul) for i in own_vector]
new_vector_X = Matrix(3, 1, new_vector_values)


print(round(im(Z).n(), 3))
print(round(re(new_vector_X[1]), 3))
'''


def Cartesian(Point1: str, Point2: str, Point3: str) -> str:
  return f'''
# Первое решение:\n
  
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

# Второе решение:\n

A = {list(Point1)}
B = {list(Point2)}
C = {list(Point3)}
urav_pryamoy_BC = ((x - B[0]) / (C[0] - B[0])) - ((y - B[1]) / (C[1] - B[1]))

tochka_x = A[0] + urav_pryamoy_BC.coeff(x) * t
tochka_y = A[1] + urav_pryamoy_BC.coeff(y) * t
t_numerical = solve(urav_pryamoy_BC.subs({{x:tochka_x, y:tochka_y}}))[0]
D = [tochka_x.subs({{t:t_numerical}}), tochka_y.subs({{t:t_numerical}})]
urav_pryamoy_BC.subs({{'x:tochka_x, y:tochka_y'}})

print(round(D[0], 3))
print(round(D[1], 3))
print(round(Point(A).distance(D), 3))
'''
