#Python – Maximum and Minimum K elements in Tuple

tup = (3, 7, 1, 18, 9)

k=int(input("Enter k : "))

#k=2

tup = sorted(tup)


    
ans = tup[:k]
ans.extend(tup[-k:])

print(ans)