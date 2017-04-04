#Write a library that contains a class that can represent any 2𝑥2 real matrice. 
#Include two functions to calculate the sum and product of two matrices. 
#Next, write a program that imports this library module and use it to perform calculations.
#Examples:
#
# matrix_1 = Matrix(4,5,6,7)
# matrix_2 = Matrix(2,2,2,1)
#
# matrix_3 = matrix_2.add(matrix_1)
#
#Try to expand your implementation as best as you can. 
#Think of as many features as you can, and try implementing them.
#(If you want you can expand implementation to NxN matrix.)
#Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
#Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
#The goal of this task is for you to SHOW YOUR BEST python programming skills.
#Impress everyone with your skills, show off with your code.
#
#When you are done upload this code to your github repository. 
#The whole repository MUST be a fork from https://github.com/mwmajew/2017sum_era1_kol1
#
#Delete these comments before commit!
#Good luck.
print("First matrix:")
# 2x2 matrix
matrix = []
for number in range(2):
    matrix.append([])
for list in matrix:
    for number in range(2):
        number2 = int(raw_input("Please enter fist matris numbers:"))
        list.append(number2)
# check if exist
for list in matrix:
    for number in list:
        print number,
    print



print("Second matrix:")
# 2x2 matrix
matrix2 = []
for number1 in range(2):
    matrix2.append([])
for list in matrix2:
    for number1 in range(2):
        number22 = int(raw_input("Please enter second matrix numbers:"))
        list.append(number22)
# check if exist
for list in matrix2:
    for number1 in list:
        print number1,
    print

#sum
print("Sum of two matrix:")
matrix3=matrix+matrix2
print matrix3

summatrix = []
summatrix=matrix+matrix2
print(summatrix)

