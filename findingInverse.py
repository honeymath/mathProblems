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

X = json.loads(input())#matrixlist

if len(X)!=1:
  raise Exception(f"You should enter exactly one matrix, but {len(X)} many matrices are detected") #score = 0.1

userMatrix = Matrix(X[0])

if userMatrix.cols!= n:
  raise Exception(f"Your matrix must have {n} columns, but now your matrix have {userMatrix.cols} columns") #score=0.3

if userMatrix.rows!= n:
  raise Exception(f"Your matrix must have {n} rows, but now your matrix have {userMatrix.rows} rows") #score = 0.6
  
 
verification = rf"""
$$\underbrace{{{latex(givenMatrix)}}}_A\times {latex(userMatrix)} = {latex(givenMatrix*userMatrix)}$$
"""




if(givenMatrix*userMatrix!=eye(3)):
  raise Exception(rf"You have suggest that $$A^{{-1}}={latex(userMatrix)}$$. However, {verification}") #score=0.9

print(rf"You have suggest that $$A^{{-1}}={latex(userMatrix)}$$")
print(rf"We verify your result {verification}")






