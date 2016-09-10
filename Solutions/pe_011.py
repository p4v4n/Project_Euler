# project euler-011

input_list=[]
for i in range(20):
    line=input()
    a=[int(x) for x in line.strip().split()]
    for num in a:
        input_list.append(num)

product_list=[]

for i in range(400):
    if i%20<=16:
        r=input_list[i]*input_list[i+1]*input_list[i+2]*input_list[i+3]
        product_list.append(r)
    if i<=339:
        d=input_list[i]*input_list[i+20]*input_list[i+40]*input_list[i+60]
        product_list.append(d)
    if i%20<=16 and i<=336:
        rd=input_list[i]*input_list[i+21]*input_list[i+42]*input_list[i+63]
        product_list.append(rd)
    if i%20>=3 and i<=339:
        ld=input_list[i]*input_list[i+19]*input_list[i+38]*input_list[i+57]
        product_list.append(ld)
        
print(max(product_list))

