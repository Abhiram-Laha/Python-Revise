#Python program to interchange first and last elements in a list

k = [12, 35, 9, 56, 24]

a = 1
b = 2

k[a-1],k[b-1] = k[b-1],k[a-1] 

print(k)