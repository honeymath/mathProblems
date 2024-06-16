# mathProblems

This project aims to provide an example representative repository for Math Problem Bank developed for honeymath.com

Honeymath is intended to hold platform-independent python-based math problems. Here is the repository for honeymath [HoneyMath Platform](https:github.com/honeymath/honeyplatform)

The code for problems is python, dispite you need to put #command(parameters) when communicating with the platform. There are following examples

For example, the following code means the platform to use matrixlist module to collect input of user
```
input()#matrixlist
```

The following code give partial credit to students when an answer is graded wrong. The `score(0.7)` means 70% partial credits were given.
```
raise Exception("Your answer is wrong, but you are given partial credits")#score(0.7)
```

The goal of the project is being able to produce such problem scripts by large language models. Instead of collecting a nice problem bank. We need effort and people to develop fine-tuned model for teachers to develop a problem easily.


## Developed problems
[1+1](1+1.py)
[Finding The inverse matrix](findingInverse.py)
[Solving Linear Equations](solveEquations.py)
[Finding Basis](basisEquations.py)
[Find pairwise linearly independent vectors](pairwiseIndependentDependentVectors.py)
[Eigenvalue and Eigenvectors](eigenvalueEigenvector.py)
[Semi Positive Definite](Example/semiPositiveDefinite.py)
[Semi Positive Definite](Example/semiPositiveDefinite_Exercise.py)
[Semi Positive Definite](Example/semiPositiveDefinite_Grading.py)
[Semi Positive Definite](Example/semiPositiveDefinite_Solution.py)
