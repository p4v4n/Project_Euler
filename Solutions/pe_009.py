# project euler-009

def special_pythagorean(n):
    triplet_list=[-1]
    for x in range(1,n//3+1):
        y=n*(n-2*x)//(2*(n-x))
        z=n-x-y
        if x**2+y**2==z**2:
            triplet_list.append(x*y*z)
    return max(triplet_list)

t=int(input())

for i in range(t):
    n=int(input())
    print(special_pythagorean(n))
