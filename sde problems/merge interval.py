stack1 = list(map(int,input().split()))
stack2=  list(map(int,input().split()))


for i in range(len(stack1)):
    if stack1[i] > stack2[0]:
        stack1[i],stack2[0] = stack2[0],stack1[i] 
        stack2.sort()

print(stack1)
print(stack2)
