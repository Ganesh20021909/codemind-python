n=int(input())
s=0
for i in range(1,n+1):
    t=1/i
    s=s+t
a="{:.2f}".format(s)
print(a)