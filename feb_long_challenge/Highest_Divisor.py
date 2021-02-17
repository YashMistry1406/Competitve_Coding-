n= int(input())
max_i=0
for i in range(1,11):
    if n%i==0 and i>max_i:
        max_i=i
    else:
        continue
print(max_i)


