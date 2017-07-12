#project euler-005

def gcd(a,b):
    a,b=max(a,b),min(a,b)
    while b!=0:
        a,b=b,a%b
    return a

def lcm_all(n):
    lcm=1
    for i in range(1,n+1):
        lcm=lcm*i//gcd(lcm,i)
    return lcm

t=int(input())

for i in range(t):
    n=int(input())
    print(lcm_all(n))
