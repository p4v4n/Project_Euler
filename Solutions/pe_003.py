# project euler-003

def largest_prime_factor(n):
    lpf=1
    f=2
    while f*f<=n:
	    while n%f==0:
	        n=n/f
	        lpf=f
	    f+=1
    if n>1:
        lpf=n
    return int(lpf)

t=int(input())

for i in range(t):
    n=int(input())
    print(largest_prime_factor(n))
