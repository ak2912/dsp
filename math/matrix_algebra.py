# Matrix Algebra
from numpy import matrix

#1.1
A = matrix([[1,2,3],[3,7,4]])
A.shape
#(2, 3)

#1.2
B = matrix([[1,-1],[0,1]])
B.shape
#(2, 2)

#1.3
C = matrix([[5,-1],[9,1],[6,0]])
C.shape
#(3, 2)

#1.4
D = matrix([[3,-2,-1],[1,2,3]])
D.shape
#(2, 3)

#1.5
u = matrix([6,2,-3,5])
u.shape
#(1, 4)

#1.6
w = matrix([[1],[8],[0],[5]])
w.shape
#(4, 1)

#2.1
v = matrix([3,5,-1,4])
v.shape

u+v
#matrix([[ 9,  7, -4,  9]])

#2.2
u-v
#matrix([[ 3, -3, -2,  1]])

#2.3
6*u
#matrix([[ 36,  12, -18,  30]])

#2.4
#undefined!

#2.5
abs(u)
#matrix([[6, 2, 3, 5]])

#3.1
#undefined!

#3.2
A-C.transpose()
#matrix([[-4, -7, -3],
#        [ 4,  6,  4]])

#3.3
C.transpose()+3*D

#matrix([[14,  3,  3],
#        [ 2,  7,  9]])

#3.4
B*A

#matrix([[-2, -5, -1],
#        [ 3,  7,  4]])

#3.5
#undefined!

