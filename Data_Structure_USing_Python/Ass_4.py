# We represent scores of batsmen across a sequence of matches in a two level dictionary as follows:
# {'match1':{'player1':57, 'player2':38}, 'match2':{'player3':9, 'player1':42}, 'match3':{'player2':41, 'player4':63, 'player3':91}
# Each match is identified by a string, as is each player. The scores are all integers. The names associated with the matches are not fixed (here they are 'match1', 'match2', 'match3'), nor are the names of the players. A player need not have a score recorded in all matches.
# Define a Python function orangecap(d) that reads a dictionary d of this form and identifies the player with the highest total score. Your function should return a pair (playername,topscore) where playername is a string, the name of the player with the highest score, and topscore is an integer, the total score of playername.
# The input will be such that there are never any ties for highest total score.
# For instance:
# >>> orangecap({'match1':{'player1':57, 'player2':38}, 'match2':{'player3':9, 'player1':42}, 'match3':{'player2':41, 'player4':63, 'player3':91}})
# ('player3', 100)
# >>> orangecap({'test1':{'Ashwin':84, 'Kohli':120}, 'test2':{'Ashwin':59, 'Pujara':42}})
# ('Ashwin', 143)




# Let us consider polynomials in a single variable x with integer coefficients. For instance:
# 3x4 - 17x2 - 3x + 5
# Each term of the polynomial can be represented as a pair of integers (coefficient,exponent). The polynomial itself is then a list of such pairs.
# We have the following constraints to guarantee that each polynomial has a unique representation:
# Terms are sorted in descending order of exponent
# No term has a zero cofficient
# No two terms have the same exponent
# Exponents are always nonnegative
# For example, the polynomial introduced earlier is represented as:
# [(3,4),(-17,2),(-3,1),(5,0)]
# The zero polynomial, 0, is represented as the empty list [], since it has no terms with nonzero coefficients.
# Write Python functions for the following operations:
# addpoly(p1,p2)
# multpoly(p1,p2)
# that add and multiply two polynomials, respectively.
# You may assume that the inputs to these functions follow the representation given above. Correspondingly, the outputs from these functions should also obey the same constraints.
# You can write auxiliary functions to "clean up" polynomials – e.g., remove zero coefficient terms, combine like terms, sort by exponent etc. Build a library of functions that can be combined to achieve the desired format.
# You may also want to convert the list representation to a dictionary representation and manipulate the dictionary representation, and then convert back.
# Some examples:
  
#    >>> addpoly([(4,3),(3,0)],[(-4,3),(2,1)])
#    [(2, 1),(3, 0)]
#    Explanation: (4x^3 + 3) + (-4x^3 + 2x) = 2x + 3
#    >>> addpoly([(2,1)],[(-2,1)])
#    []
#    Explanation: 2x + (-2x) = 0
#    >>> multpoly([(1,1),(-1,0)],[(1,2),(1,1),(1,0)])
#    [(1, 3),(-1, 0)]
#    Explanation: (x - 1) * (x^2 + x + 1) = x^3 - 1



def orangecap(d):
  total={}
  for match in d.keys():
    for player in d[match].keys():
      try:
        total[player]+=d[match][player]
      except:
        total[player]=d[match][player]
  maxi=(-1,-1)
  for player,score in total.items():
    if(score>maxi[1]):
      maxi=(player,score)
  return maxi

def addpoly(p1,p2):
    result=[]
    i1,i2=0,0
    l1,l2=len(p1),len(p2)
    while(i1<l1 and i2<l2):
        if(p1[i1][1]>p2[i2][1]):
            result.append(p1[i1])
            i1+=1
        elif(p1[i1][1]<p2[i2][1]):
            result.append(p2[i2])
            i2+=1
        else:
            if(p1[i1][0]+p2[i2][0]!=0):
                result.append((p1[i1][0]+p2[i2][0],p1[i1][1]))
            i1+=1
            i2+=1
    while(i1<l1):
        result.append(p1[i1])
        i1+=1
    while(i2<l2):
        result.append(p2[i2])
        i2+=1
    return result

def multpoly(p1,p2):
    result_dict=dict()
    for coeff1,exp1 in p1:
        for coeff2,exp2 in p2:
            try:
                result_dict[exp1+exp2] += coeff1*coeff2
            except:
                result_dict[exp1+exp2] = coeff1*coeff2
    return sorted([(coeff,exp) for exp,coeff in result_dict.items() if coeff!=0],key=lambda x: x[1],reverse=True)