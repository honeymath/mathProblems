

import random
from sympy import Matrix, latex, eye
import json


scale = 4 # scale of randomness of the matrix entry
n = 3 # The size of the matrix.

## The following code generates an upper triangular matrix
upper = [[1 if i == j else 0 if i < j else int(random.random()*scale) for j in range(n)] for i in range(n)]

## The following code generates an lower triangular matrix
lower = [[1 if i == j else 0 if i > j else int(random.random()*scale) for j in range(n)] for i in range(n)]

## The following code, using fisher's shuffle algorithm, generates a partition of [0,...,n-1]
switch = list(range(n))
for i in range(n):
    k = int(random.random()*(n-i))
    switch[i],switch[k] = switch[k],switch[i]

    
## The following code generates a switching matrix
swi = [[1 if i == switch[j] else 0 for i in range(n)]for j in range(n)]
  

## Pack the above into matrices that can be processed by sympy
up = Matrix(upper)
lo = Matrix(lower)
sw = Matrix(swi)

## The following code generates a random vector

theb = [[int(random.random()*scale)] for i in range(n)]

b = Matrix(theb)

## The following matrix is going to give the student as content of exercise

givenMatrix = sw*up*lo

variables = ['x','y','z','u','v','w','s','t','r','p','q']
cols = len(givenMatrix.tolist()[0])

print("Solve the following equations")

if cols <= len(variables):
  variable_matrix = Matrix([[i] for i in variables[:cols]])
else:
  variable_matrix = Matrix([[f"x_{i}"] for i in range(cols)])

equations = givenMatrix*variable_matrix

equationList = equations.tolist()

for i in range(n):
  print(f"$${latex(equationList[i][0])} = {theb[i][0]}$$")

print(rf"Please give a matrix M such that $${latex(variable_matrix)} = M$$ is a solution")


X = json.loads(input())#matrix

if len(X)!=1:
  raise Exception(f"You should enter exactly one matrix, but {len(X)} many matrices are detected")
  
if len(X[0])!= n:## check the number of cols
  raise Exception(f"Your matrix must have {n} rows, but now your matrix have {len(X[0])} rows")

if len(X[0][0])!= 1:
  raise Exception(f"Your matrix must have 1 cols, but now your matrix have {len(X[0][0])} columns")
  
userInput =Matrix( X[0])
print(rf"By what you have entered, you mean $$M={latex(userInput)}$$")

verifyb = givenMatrix * userInput



if verifyb == b:
  print(rf"Let us verify your solution is correct. Indeed $${latex(givenMatrix)}\times {latex(userInput)} = {latex(verifyb)},$$ which means your answer is a solution")
else:
  raise Exception(rf"However, I have calculated $${latex(givenMatrix)}\times {latex(userInput)} = {latex(verifyb)}$$")



