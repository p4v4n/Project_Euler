# project euler-15

def no_of_ways(m,n):
    k,l=max(m,n),min(m,n)
    num=1
    den=1
    for i in range(l):
        num*=(k+1+i)
        den*=(i+1)
    final=num//den
    return final%1000000007

t=int(input())

for i in range(t):
    n=[int(x) for x in input().split()]
    print(no_of_ways(n[0],n[1]))
