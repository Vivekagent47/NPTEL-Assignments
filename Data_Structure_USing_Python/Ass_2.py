def threesquares(n):
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

def hillvalley(l):
    inc,dec=1,1
    i,j=0,1
    n=len(l)
    flow='inc'
    while(j<n):
        if(l[i]>l[j] and flow=='inc'):
            inc=inc+1
        elif(l[i]<l[j] and flow=='inc'):
            flow='dec'
            dec=dec+1
        elif(l[i]<l[j] and flow=='dec'):
            dec=dec+1
        else:
            return False
        i,j=i+1,j+1
    if(inc>=2 and dec>=2):
        return True
    return False