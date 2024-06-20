#!/bin/python3

import math
import os
import random
import re

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    sumRight = 0
    sumLeft = 0
    counterR = 0
    counterL = 1
    
    for elem in arr[1:]:
        sumRight+= elem[counterR]
        counterR+=1
        sumLeft += elem[-counterL]
        counterL+=1
    ans = abs(sumRight-sumLeft)
    print(ans)
    return ans
arr = [[3],[11,2,4],[4,5,6],[10,8,-12]]

print(diagonalDifference(arr))