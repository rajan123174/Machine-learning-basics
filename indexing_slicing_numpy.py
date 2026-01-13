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
print(arr[1,:]) 
print(arr[arr > 25]) 

'''
Reshaping and Manipulating Arrays
arr.reshape()
'''





