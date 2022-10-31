a=int(input())
k=a
h=[]
if a<0:
    a=a*(-1)
while a:
    t=a%10
    a//=10
    if t!=0:
        h.append(str(t))
n=("".join(h))
if k<0:
    q=int(n)
    print(q*-1)
else:
    print(n)