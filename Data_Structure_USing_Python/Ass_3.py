# Define a Python function remdup(l) that takes a nonempty list of integers l and removes all duplicates in l, keeping only the first occurrence of each number. For instance:
# >>> remdup([3,1,3,5])
# [3, 1, 5]
# >>> remdup([7,3,-1,-5])
# [7, 3, -1, -5]
# >>> remdup([3,5,7,5,3,7,10])
# [3, 5, 7, 10]



# Write a Python function sumsquare(l) that takes a nonempty list of integers and returns a list [odd,even], where odd is the sum of squares all the odd numbers in l and even is the sum of squares of all the even numbers in l.
# Here are some examples to show how your function should work.
# >>> sumsquare([1,3,5])
# [35, 0]
# >>> sumsquare([2,4,6])
# [0, 56]
# >>> sumsquare([-1,-2,3,7])
# [59, 4]




# A two dimensional matrix can be represented in Python row-wise, as a list of lists: each inner list represents one row of the matrix. For instance, the matrix
# 1  2  3  4
# 5  6  7  8
# would be represented as [[1, 2, 3, 4], [5, 6, 7, 8]].
# The transpose of a matrix converts each row into a column. The transpose of the matrix above is:
# 1  5
# 2  6
# 3  7
# 4  8
# which would be represented as [[1, 5], [2, 6], [3, 7], [4, 8]].
# Write a Python function transpose(m) that takes as input a two dimensional matrix m and returns the transpose of m. The argument m should remain undisturbed by the function.
# Here are some examples to show how your function should work. You may assume that the input to the function is always a non-empty matrix.
# >>> transpose([[1,2,3],[4,5,6]])
# [[1, 4], [2, 5], [3, 6]]
# >>> transpose([[1],[2],[3]])
# [[1, 2, 3]]
# >>> transpose([[3]])
# [[3]]


def remdup(lst):
    return list(dict.fromkeys(lst))



def sumsquare(lst):
    sumeven = 0
    sumodd = 0
    for i in range(0,len(lst)):
        if lst[i]%2 == 0:
            sumeven = sumeven + lst[i]**2
        else :
            sumodd = sumodd + lst[i]**2
    return [sumodd,sumeven]   
  
  
def transpose(anArray):
    result = [[anArray[j][i] for j in range(len(anArray))] for i in range(len(anArray[0]))]
    return result
