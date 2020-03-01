# A positive integer m can be expresseed as the sum of three squares if it is of the form p + q + r where p, q, r ≥ 0, and p, q, r are all perfect squares. 
# For instance, 2 can be written as 0+1+1 but 7 cannot be expressed as the sum of three squares. 
# The first numbers that cannot be expressed as the sum of three squares are 7, 15, 23, 28, 31, 39, 47, 55, 60, 63, 71, … (see Legendre's three-square theorem).
# Write a Python function threesquares(m) that takes an integer m as input and returns True if m can be expressed as the sum of three squares and False otherwise. 
# (If m is not positive, your function should return False.)
# Here are some examples of how your function should work.
# >>> threesquares(6)
# True
# >>> threesquares(188)
# False
# >>> threesquares(1000)
# True




# Write a function repfree(s) that takes as input a string s and checks whether any character appears more than once. The function should return True if there are no repetitions and False otherwise.
# Here are some examples to show how your function should work.
# >>> repfree("zb%78")
# True
# >>> repfree("(7)(a")
# False
# >>> repfree("a)*(?")
# True
# >>> repfree("abracadabra")
# False




# A list of numbers is said to be a hill if it consists of an ascending sequence followed by a descending sequence, where each of the sequences is of length at least two. Similarly, a list of numbers is said to be a valley hill if it consists of an descending sequence followed by an ascending sequence. You can assume that consecutive numbers in the input sequence are always different from each other.
# Write a Python function hillvalley(l) that takes a list l of integers and returns True if it is a hill or a valley, and False otherwise.
# Here are some examples to show how your function should work.
# >>> hillvalley([1,2,3,5,4])
# True
# >>> hillvalley([1,2,3,4,5])
# False
# >>> hillvalley([5,4,1,2,3])
# True
# >>> hillvalley([5,4,3,2,1])
# False



def threesquares(n):
    if n >= 0:
        for i in range(0,n):
            for j in range(0,n):
                for k in range(0,n):
                    if i**2 + j**2 + k**2 == n:
                        return True
    return False


def repfree(s):
    for i in range(0,len(s)):
        for j in range(i+1,len(s)):
            if s[i] == s[j]:
                return False
    return True  

# def hillvalley(l):
#     inc,dec=1,1
#     i,j=0,1
#     n=len(l)
#     flow='inc'
#     while(j<n):
#         if(l[i]>l[j] and flow=='inc'):
#             inc=inc+1
#         elif(l[i]<l[j] and flow=='inc'):
#             flow='dec'
#             dec=dec+1
#         elif(l[i]<l[j] and flow=='dec'):
#             dec=dec+1
#         else:
#             return False
#         i,j=i+1,j+1
#     if(inc>=2 and dec>=2):
#         return True
#     return False


def ascending(l):
    if len(l) <= 1:
        return(True)
    else:
        return(l[0] < l[1] and ascending(l[1:]))

def descending(l):
    if len(l) <= 1:
        return(True)
    else:
        return(l[0] > l[1] and descending(l[1:]))

def hill(l):
    for i in range(1,len(l)-1):
        if ascending(l[:i+1]) and descending(l[i:]):
            return(True)
    return(False)

def valley(l):
    for i in range(1,len(l)-1):
        if descending(l[:i+1]) and ascending(l[i:]):
            return(True)
    return(False)

def hillvalley(l):
    return(hill(l) or valley(l))
