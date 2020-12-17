'''Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.'''

def moveZeroes(a):
  for i in range(1,len(a)):
    va = a[i]
    hole = i
    while ((hole > 0) & (a[hole-1]==0) & (va!=0)):
      a[hole] = a[hole-1]
      hole = hole-1
    a[hole] = va
  return a

