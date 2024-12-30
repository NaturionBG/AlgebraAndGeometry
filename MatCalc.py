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
  print(name**varName)
  if name**varName == {btrace}:
    break'''
      
def BigMatrices(order: int, diagstart: int, diagend: int, a12: int = None, a21: int = None, row1end: int = None) -> str:
  if row1end!=None:
    return f'''
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

print(VarName3, trace(MatrixName2)+sum(listName2))'''
    