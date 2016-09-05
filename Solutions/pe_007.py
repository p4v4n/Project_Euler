#project euler-007

def prime_check(n):
    a=int(n**0.5)
    for i in range(2,a+1):
        if n%i==0:
            return False
    return True

prime_list=[2]
i=3

while len(prime_list)<=10000:
    if prime_check(i):
        prime_list.append(i)
    i+=2

t=int(input())

for i in range(t):
    n=int(input())
    print(prime_list[n-1])
