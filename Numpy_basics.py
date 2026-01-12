import numpy as np

a = np.array([1,2,3]) # 1d Array
print(a)

b = np.array([[9.0,10.2,22.3,11],[6.0,5.5,6.6,7.8]])
print(b) # 2d Array

a_dimention = a.ndim # To get dimention of an array
print(a_dimention)

b_dimention = b.ndim
print(b_dimention) # To get dimention of an array

a_shape = a.shape # to get shape of an array
print(a_shape)

b_shape = b.shape # to get shape of an array
print(b_shape)

a_type = a.dtype # to get type of an array
print(a_type)

b_type = b.dtype # to get type of an array 
print(b_type)

a_size = a.itemsize # size of an array in bytes
print(a_size)

b_size = b.itemsize
print(b_size)

a_size2 = a.size # no elements in an arrray
print(a_size2)

b_size2 = b.size
print(b_size2)

total_size_a = a_size*a_size2 # total size of an array in memory
print(total_size_a)

total_size_b = b_size*b_size2
print(total_size_b)

totalSize_a = a.nbytes # total size of as array in memory
totalSize_b = b.nbytes
print(totalSize_a,totalSize_b)

'''
Accessing/Changing specific elements
,Rows, Columns,etc'''

# To get a specific element

a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
Nine = a[1,1] 
print(Nine) # to get 9 'array_name[r, c]'

# To get a specific row 

row1 = a[0,:] # here (:) means all columns [rowindex,columnindex]
print(row1)

# to get a specific column

column1 = a[: ,2]
print(column1)

# Getting a litle more fancy [sta-index: end-index: step-index]
smart_fetching = a[1, 1:6:2] #[row-idx, st-idx:st-idx:step-idx]
print(smart_fetching)

# 3-dimentional array
c = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])# 3d array
print(c)

four = c[0,1,1]
print(four)

# zeroes array
zeroes = np.zeros((2,3))
print(zeroes)

# ones array
ones = np.ones((2,3))
print(ones)

# Full function -> to create an array with specific elements
# full(shape,value)
filled_array = np.full((2,3),7)
print(filled_array)

# to get sequence of numbers like range in python 
arr = np.arange(1,10,2)
print(arr)#arange(st,stp,step)

# to print identity matrix that is a squal matrix of 1 in diagonal and rest are zeros
identity_mat = np.eye(4)
print(identity_mat)

# to get information about data type of an array
arr_dtype = np.array([10,20,30])
print(arr_dtype.dtype)

# to chage to a datatype from a datatype
#syntax-> arr.astype(new_type)
arr2 = np.array([1.2,1.3,1.4,1.5,1.6,1.7])
intarr = arr2.astype(int)
print(intarr)

# Mathematicals operations performed in numpy
'''
Operator            example
+                   arr+2
-                   arr-2      
*                   arr*2
/                   arr/2
**                  arr**2
//                  arr//2
%                   arr%2
'''

arr3 = np.array([10,20,30,40,50,60,70])
print(arr3+5)

'''
Aggregation Function
fnction                what does
np.sum(arr)           calculates sum
np.mean(arr)          give avg of arry
np.min(arr)           give minimum of arr
np.max(arr)           give max of array
np.std(arr)           give standard deviation of array
np.var(arr)           gives variance of array
'''

print(np.sum(arr3))           
print(np.mean(arr3))          
print(np.min(arr3))           
print(np.max(arr3))           
print(np.std(arr3))           
print(np.var(arr3)) 

