# project euler-004

plist=[]

for x in range(100,1000):
    for y in range(100,1000):
	    p=x*y
	    if len(str(p))==6 and str(p)==str(p)[::-1]:
		    if p not in plist:
		        plist.append(p)

sorted_list=sorted(plist)		   

def largest_palindrome(n):
    for i in range(len(sorted_list)):
	    if sorted_list[i]>=n:
		    return sorted_list[i-1]
		    break

t=int(input())

for i in range(t):
    n=int(input())
    print(largest_palindrome(n))
