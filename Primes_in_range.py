def prime(n):
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    else:
        return True
a=int(input())
b=int(input())
count=0
for i in range(a,b+1):
    if prime(i):
        count=count+1
print(count)