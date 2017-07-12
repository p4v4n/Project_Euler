# project euler-008

def largest_product(n,k): 
    product_list=[]
    for i in range(0,n-k+1):
        Product=1
        for j in range(i,i+k):
            Product*=int(D[j])
        product_list.append(Product)
    return max(product_list)
    
t=int(input())

for i in range(t):
    a=[int(x) for x in input().split()]
    N=a[0]
    K=a[1]
    D=str(input())
    print(largest_product(N,K))
