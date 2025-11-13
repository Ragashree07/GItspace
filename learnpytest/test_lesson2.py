def dups(n):
    dc={}
    for x in n:
        dc[x]=dc.get(x,0)+1
    return dc
print(dups([1,1,2,3,4,4]))