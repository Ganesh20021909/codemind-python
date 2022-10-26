a,b,c=map(int,input().split())
t=a*(pow((1+b/100),c))
e="{:.2f}".format(t)
print(e)