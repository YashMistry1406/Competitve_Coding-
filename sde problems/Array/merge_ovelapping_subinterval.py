n = int(input())
stack = [[int(input()) for _ in range(2)] for m in range(n)]
ans = []
temp =[]
for i in range(0,n-1):
    if stack[i][0] < stack[i+1][0]:
        if stack[i][1] < stack[i+1][1] and stack[i][1] >= stack[i+1][0]:
            temp.append(stack[i][0])
            temp.append(stack[i+1][1])
            print(temp)
        else:
            ans.append(temp)
            temp = []
print(ans)