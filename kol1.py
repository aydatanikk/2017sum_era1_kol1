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
def addMatrix(matrix1,matrix2):
    res=[][]
    a=0
    for	a in range (2)
		b=0	
		for b in range (2)
			res[a][b]=matrix1[a][b]+matrix2[a][b]
return res

def subMatrix(matrix1,matrix2):
    res=[][]
    a=0
    for	a in range (2)
		b=0	
		for b in range (2)
			res[a][b]=matrix1[a][b]-matrix2[a][b]
return res 


def mulMatrix(matrix1,matrix2):
    res=[][]
    a=0
    for	a in range (2)
		b=0	
		for b in range (2)
			res[a][b]=matrix1[a][b]*matrix2[a][b]
return res 
    
class TestMatrix:
    print("Additon of matrix\n")
    matrix1=[2][4]
    matrix2=[3][5]
    result=addMatrix(matrix1,matrix2);
    print(result)
    
    print("Subtraction of matrix\n")
    matrix1=[2][4]
    matrix2=[3][5]
    result=subMatrix(matrix1,matrix2);
    print(result)
    
    print("Multiplication of matrix\n")
    matrix1=[2][4]
    matrix2=[3][5]
    result=mulMatrix(matrix1,matrix2);
    print(result)
    
    
    

