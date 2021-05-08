#Method 2 for Maxpooling using NumPy

#import the required packages
import numpy as np

# Number of Rows and Columns are given as input
R = int(input("enter number of rows: "))
C = int(input("Enter number of coluns: "))

i,j = 0 , 0

max_els=[]

#Checks if R is equal to C or not, since we're performing this operation on symmetric matrices.
if (R != C):
  print("enter a symmetric matrix")

#if the R is equal to C then we perform the following operations
else:
  print("enter elements")
  elements = list(map(int, input().split()))

  matrix = np.array(elements).reshape(R,C)
  print(matrix)
#enter the pooling size of matrix, for 4x4 I would enter the pooling matrix size as 2x2
  pool_r = int(input("Enter row size for pooling: "))
  pool_c = int(input("Enter column sixe for pooling: "))

  if (pool_r <= R/2 and pool_c <= C/2):
    if (pool_r == pool_c):
      while (i<R):
        j=0
        while (j<C):
          temp = matrix[i:i+pool_r, j:j+pool_c]
          j += pool_c
          print(temp)
          max_el = temp.max()
          print(max_el)
          max_els.append(max_el)

        i += pool_r

print(max_els)

#maxpooled matrix
pooled_matrix = np.array(max_els).reshape(pool_r,pool_c)
print(pooled_matrix)
