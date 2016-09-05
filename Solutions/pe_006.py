#project euler-006

def sum_square_diff(n):
    sd=n*n*(n+1)*(n+1)//4 -n*(n+1)*(2*n+1)//6
    return sd
    
t=int(input())

for i in range(t):
    n=int(input())
    print(sum_square_diff(n))
