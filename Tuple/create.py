# Python program to create a list of tuples from given list having number and its cube in each tuple

l = [9, 5, 6,7,4]

ans =[]

for i in l:
    a=i**2
    m = (i,a)
    ans.append(m)
    
print(ans)