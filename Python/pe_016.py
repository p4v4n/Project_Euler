# project euler-16
power=1
power_list=[1]
for i in range(10**4):
    power*=2
    power_list.append(str(power))
    
def sum_of_digits(n):
    sum=0
    for i in range(len(power_list[n])):
        sum+=int(power_list[n][i])
    return sum

t=int(input())

for i in range(t):
    n=int(input())
    print(sum_of_digits(n))
