from itertools import groupby

t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    res = [(key, len(list(group))) for key, group in groupby(a)]
    
     
     





  
   
 







