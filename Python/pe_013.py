# project euler-013

N=int(input())
list_of_lists=[]
for i in range(N):
    n=list(input())
    list_of_lists.append(n)
final_list=[]
counter=0
for i in range(50):   
    for j in range(N):
        counter+=int(list_of_lists[j][49-i])
    remainder=counter%10
    counter=counter//10
    final_list.append(str(remainder))
    
final_sum_list=str(counter)+''.join(final_list)[::-1]

print(int(final_sum_list[:10]))
