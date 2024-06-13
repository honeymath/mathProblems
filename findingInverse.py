import random
from sympy import Matrix, latex, eye
from sympy.combinatorics import Permutation
import json


scale = 4 # scale of randomness of the matrix entry
n = 3 # The size of the matrix.

## The following code generates an upper triangular matrix
upper = [[1 if i == j else 0 if i < j else int(random.random()*scale) for j in range(n)] for i in range(n)]

## The following code generates an lower triangular matrix
lower = [[1 if i == j else 0 if i > j else int(random.random()*scale) for j in range(n)] for i in range(n)]

## The following code, we generate a random switching matrix.
switch = list(range(n))
random.shuffle(switch)
sw = eye(n)[switch,:]

  

## Pack the above into matrices that can be processed by sympy
up = Matrix(upper)
lo = Matrix(lower)


## The following matrix is going to give the student as content of exercise

givenMatrix = sw*up*lo

print("Please find the inverse of the following matrix.")
print(f"$$A={latex(givenMatrix)}$$")

X = json.loads(input())#matrix

if len(X)!=1:
  raise Exception(f"You should enter exactly one matrix, but {len(X)} many matrices are detected")
  
if len(X[0])!= n:
  raise Exception(f"Your matrix must have {n} columns, but now your matrix have {len(X[0])} columns")

if len(X[0][0])!= n:
  raise Exception(f"Your matrix must have {n} rows, but now your matrix have {len(X[0][0])} columns")
  
 



user = Matrix(X[0])


if(givenMatrix*user!=eye(3)):
  raise Exception(rf"You have suggest that $$A^{{-1}}={latex(user)}$$. However, based on my calculation. $$\underbrace{{{latex(givenMatrix)}}}_A\times {latex(user)} = {latex(givenMatrix*user)}$$")

print(rf"You have suggest that $$A^{{-1}}={latex(user)}$$")
print(rf"We verify your result $$\underbrace{{{latex(givenMatrix)}}}_A\times {latex(user)} = {latex(givenMatrix*user)}$$ ")





