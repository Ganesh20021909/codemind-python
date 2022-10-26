a,b=map(int,input().split())
c=min(a,b)
d=max(a,b)
r=d-c
if r==1 or r==9:
    print("Yes")
else:
    print("No")