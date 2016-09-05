# project euler-001

def sum(a,n):
    b=int((n-1)/a)
    s=a*b*(b+1)//2
    return int(s)
    
t=int(input())

for i in range(0,t):
    n=int(input())
    print(int(sum(3,n)+sum(5,n)-sum(15,n)))
