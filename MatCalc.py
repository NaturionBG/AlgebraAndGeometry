from sympy import *
from sympy.abc import x, Y

def MatrixOps(__MatrixName1__: str, __MatrixName2__: str, OPS: list[str]) -> str:
  if 'kron' in OPS:
    return f'''
__ResultName1__ = {__MatrixName1__}*transpose({__MatrixName2__})
__ResultName2__ = transpose({__MatrixName1__})*{__MatrixName2__}
__ResultName3__ = kronecker_product(__ResultName1__, __ResultName2__)
print(trace(__ResultName1__))
print(trace(__ResultName3__))'''
  else:
    return f'''
__ResultName1__ = {__MatrixName1__}*transpose({__MatrixName2__})
__ResultName2__ = transpose({__MatrixName1__})*{__MatrixName2__}
print(max(__ResultName1__))
print(sum(__ResultName2__))'''
  
def MatrixEquations(name1: str, name2: str, name3: str = None) -> str:
  if name3!=None:
    return f'''
pretty_print({name1}.inv()*{name3}*({name2}.inv()))'''
  else:
    return f'''
Если у вас вид: AX=B, то код: pretty_print({name1}.inv()*{name2})
Если же вид: XA=B, то код: pretty_print({name2}*({name1}.inv()))'''
    
def Deter(name1: str, name2: str = None) -> str:
  if name2!=None:
    return f'''
name3={name1}*{name2}
__equationName__ = Eq(det(name3), 0)
VarName=solve(__equationName__)
В оформлении задания на бумаге самостоятельно найдите, линейной комбинацией 
каких строк/столбцов является столбец/строка с параметром'''
  else:
    return f'''
pretty_print(det({name1}))
В оформлении задания на бумаге распишите, как вы находили определитель.'''
    
def Permute(permName: str, index: int, btrace: int) -> str:
  return f'''
name=Matrix([])
for i in {permName}:
  name=name.hstack(name, Matrix([0 if k+1!=i else 1 for k in range(len(perm))]))
  
print(name**{index})
  
for varName in range(1, 100):
  print(name**varName, varName)
  if name**varName == {btrace}:
    break'''
      
def BigMatrices(order: int, diagstart: int, diagend: int, a12: int = None, a21: int = None, row1end: int = None) -> str:
  if row1end!=None:
    return f'''
# Первое решение:\n    

VarName1={order} 
Name1={diagstart}
Name2={diagend}
Name3={row1end}

VarName2=(Name3-Name1)/(VarName1-1)
VarName3=(Name2/Name1)**(1/(VarName1-1))

diagonListName=[Name1*(VarName3**i) for i in range(VarName1)]
rowListName=[Name1 + VarName2*i for i in range(VarName1)]

inversed_diagListName=[1/i for i in diagonListName]
inversed_rowListName=[-i/k for i, k in zip(rowListName, diagonListName)]
print(sum(inversed_diagListName)+sum(inversed_rowListName[1:]))
print(min([min(inversed_diagListName), min(inversed_rowListName)]))
    '''
  else:
    return f'''
VarName1={order}
Name2={diagstart}
name3={diagend}
d=(name3-Name2)/(VarName1-1)
listName=[Name2]
for i in range(VarName1-1):
  listName.append(listName[-1]+d)
listName=listName[2:]

VarName2=1
for i in listName:
  VarName2*=i
MatrixName=Matrix([[Name2, {a12}], [{a21}, Name2+d]])
VarName3=det(MatrixName)*VarName2

listName2=[1/i for i in listName]
MatrixName2=MatrixName.inv()

print(VarName3, trace(MatrixName2)+sum(listName2))

# Второе решение:\n


dlina = {order}
a11 = {diagstart}
ann = {diagend}
a12 = {a12}
a21 = {a21}

spisochek = [i / (dlina - 1) * (ann - a11) + a11 for i in range(dlina)]
diagonal = spisochek[0] * spisochek[1] - a12 * a21
sled = (spisochek[0] + spisochek[1]) / diagonal
for i in spisochek[2:]:
  diagonal *= i
  sled += 1 / i
  
  
print(round(diagonal,3))
print(round(sled,3))
'''
    
    
def MatrixRows(StarterMatrixName: str, symb: float, m: int, n: int, f: int, lesserThan: float) -> str:
  return f'''
Первое решение:\n
  
__MatrixName__={symb}*{StarterMatrixName}

def FunctionName1(VarName1, VarName2):
  MatrixName1=zeros(2)
  for i in range(VarName1, VarName2+1):
      MatrixName1+=__MatrixName__**i
  return MatrixName1
    
def FunctionName2(VarName3):
  return (eye(2)-__MatrixName__).inv() * __MatrixName__**VarName3

for k in range(300):
  if max(FunctionName2(k))<{lesserThan}:
    print(k)
    break
print(max(FunctionName1({m}, {n})), max(FunctionName2({f})), VarName4)

# В данной задаче необходимо (В оформлении) доказать, что матрица S сходится к B.
# Комментарий к вышеизложенному: Егор, это просто жесть

# Второе решение:\n

__MatrixName__={symb}*{StarterMatrixName}

def s(m,n):
  S = zeros(2)
  for i in range(m, n + 1):
    S += A**i
  return S
  
def b(m):
    B = ((I - A).inv()) * (A**m)
    return B
  
print(max(s({m}, {n})))
print(max(b({f})))


for i in range(500):
    if max(b(i)) < {lesserThan}:
        print(i)
        break
'''


def arifm_and_geom_matrix_progression(n: int, a11: float, a1n: float, ann: float):
  f'''
a11 = {a11}
a1n = {a1n}
vsego_symbols = {n}
ann = {ann}
q = solve(ann / x ** vsego_symbols - 1, x, minimal=True)
d = (a1n - a11) / vsego_symbols
spis_stroki = [1]
spis_diag = [1]
for i in range(vsego_symbols-1):
    spis_stroki.append(spis_stroki[-1] + d)
    spis_diag.append(spis_diag[-1] * q)

spis_stroki_B = [1]
spis_diag_B = [1]
for i in range(vsego_symbols-1):
    spis_diag_B.append(1 / spis_diag[1:][i])
    spis_stroki_B.append(-spis_stroki[1:][i] / spis_diag[1:][i])

print(round(min(min(spis_stroki_B), min(spis_diag_B)), 3), round(sum(spis_diag_B) + sum(spis_stroki_B) - 1, 3))'''