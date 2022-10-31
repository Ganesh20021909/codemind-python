a=int(input())
y=1000
t=[]
p=0
q=1
for i in range(1,y):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            if i>a:
                t.append(i)
                break
            else:
                t.append(i)
m=[]
for i in t:
    i=abs(a-i)
    m.append(i)
print(min(m))