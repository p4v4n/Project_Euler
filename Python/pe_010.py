# project euler-010

def prime_check(n):
    a=int(n**0.5)
    for i in range(2,a+1):
        if n%i==0:
            return False
    return True
    
sum_primes=[0,0]
sum=0

for n in range(2,10**6):
    if prime_check(n):
	    sum+=n
    sum_primes.append(sum)

t=int(input())

for i in range(t):
    n=int(input())
    print(sum_primes[n])
