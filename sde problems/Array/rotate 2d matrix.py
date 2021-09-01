n = int(input())

arr = [[int(input()) for _ in range(n)] for k in range(n)]

for i in range(n):
    for j in range(i):
        arr[i][j],arr[j][i] = arr[j][i],arr[i][j]
for i in range(n):
    arr[i]= arr[i][::-1]
print(arr)