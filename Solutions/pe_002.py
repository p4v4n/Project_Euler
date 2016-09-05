# project euler-002

def sum(n):
    fib_seq=[1,2]
    s=2
    i=2
    while True:
        nex=fib_seq[i-2]+fib_seq[i-1]
        if nex>=n:
            break
        fib_seq.append(nex)
        if nex%2==0:
            s+=nex
        i+=1        
    return s

t=int(input())

for i in range(t):
    a=int(input())
    print(sum(a))
    
