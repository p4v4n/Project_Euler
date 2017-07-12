# project euler-012

def sum_Of_factors(n):
    a=int(n**0.5)
    sumf=1
    i=3
    while n!=1:
        count=1
        if i>a+2:
            if n!=0:
                return 2*sumf
            else:
                return sumf
        while n%2==0:
            n=n//2
            count+=1
        sumf*=count
        count=1
        while n%i==0:
            n=n//i
            count+=1
        sumf*=count
        i+=2
    return sumf
        
l=[]

i=1
while len(l)<1000: 
    a=i*(i+1)//2
    if i%2==0:
        x=sum_Of_factors(i//2)*sum_Of_factors(i+1)
    else:
        x=sum_Of_factors(i)*sum_Of_factors((i+1)//2) 
          
    l.extend(([a]*(x-len(l))))      
    i+=1
             
t=int(input())

for i in range(t):
    n=int(input())
    print(l[n])
