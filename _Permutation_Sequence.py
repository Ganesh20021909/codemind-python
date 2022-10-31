from itertools import permutations
a,b=map(int,input().split())
p=list(permutations(range(1,a+1)))
y=p[b-1]
t=[]
for i in y:
    e=str(i)
    t.append(e)
print("".join(t))