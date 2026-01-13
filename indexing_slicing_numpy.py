import numpy as np

'''
Indexing-> to select an specific element
Slicing-> to get a portion of datasets
Fancy indexing->     >2      <6     
Boolean masking

array[index] 1d array
array[rowidx,colidx] 2d array
'''

arr = np.array([[10,20,30,40,50],
                [60,70,80,90,100]])
print(arr[1,2]) 
print(arr[1,:]) # to get an specific column
print(arr[ ::-1]) # to reverse an array in Numpy
print(arr[arr > 25]) 

'''
Reshaping and Manipulating Arrays
arr.reshape()
'''
'''
reshaping doesn't create a copy it 
creates a view it affects an array'''
arr1d = np.array([10,20,30,40,50,60])
print(arr1d)
reshaped_arr = arr1d.reshape(2,3)
print(reshaped_arr)
print(arr1d)

'''
Flatttening an array 
converting multidimentional
array in a 1 dimentional
array
.ravel()-> View
.flatten()-> Copy
'''

arr3 = np.array([[10,20,30],
                 [40,50,60]])
r = arr3.ravel()
r[0] = 30
print(arr3)

f = arr3.flatten()
f[0] = 30
print(arr3)

'''
Array Modification
add-> New datapoints
remove-> unnecessary data
stack -> merzing
split ->spliting
we can use built in function to insert an ele in an array
np.insert(array,idx,elem,axis=None) -> flattened array 1d array
axis = None :-> means 1d array
axis = 0:-> row wise insert
axis = 1:-> column wise insert
np.append(arr,[40,50,60]) ;-> to add at the end doesn't change original array
np.concatenate((arr1,arr2),axis = 0)
axis = 0:-> vertical stacking(row wise)
axis = 1;-> horizontal stacking(column wise)
Removing elements of array
np.delete(array,idx,axis=None)

Stacking and Spliting
STACKING
vertically and horizontally
vstack() row wise
hstack() column wise

SPLITTING
To split an array in multiple sub array
np.split(array,parts) :-> for equal solitting
np.hsplit():-> column wise
np.vsplit():-> row wise 

'''

arr4 = np.array([1,2,3,4,5,6,7])
print(arr4)
new_arr = np.insert(arr4,2,100)
print(arr4)
print(new_arr)

arr2d = np.array([[1,2],[3,4]])
print(arr2d)
new2darray = np.insert(arr2d,2,[7,8],axis = 0)
print(new2darray)
new2darray = np.insert(arr2d,2,[7,8],axis = 1)
print(new2darray)

arr5 = np.array([10,20,30,40])
new_arr2 = np.append(arr5,[50,60,70,80])
print(new_arr2)

arr5 = np.array([1,2,3,4,5])
arr6 = np.array([6,7,8,9,10])
newarr4 = np.concatenate((arr5,arr6))
print(newarr4)

arr7 = np.array([1,2,3,4,5])#1d rray
print(np.delete(arr7,1,axis=None))

arr8 = np.array([[1,2,3],[4,5,6]])# 2d array
print(np.delete(arr8,0,axis=0))

arr9 = np.array([1,2,3,4])
arr10 = np.array([5,6,7,8])
print(np.vstack((arr9,arr10)))
print(np.hstack((arr9,arr10)))

arr11 = np.array([1,2,3,4,5,6,7,8])
print(np.split(arr11,2))
arr12 = np.array([[1,2,3],[4,5,6]])
print(np.hsplit(arr11,2))






