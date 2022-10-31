a=int(input())
b=int(input())
t=[]
for i in range(a,b+1):
    y=i
    while(y>0):
        p=y%10
        if p==0 or i%p!=0:
            break
        y//=10
    if y==0:
        t.append(i)
print(*t)