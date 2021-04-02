for t in range(int(input())):

    n,k=map(int,input().split())

    s=input()
    flag=False
    stack=[]
    for i in s:
        if i =='*':
            stack.append(i)
        if i!='*' :
            if len(stack)>=k:
                print("Yes")
                flag=True
                break
            if len(stack)!=k:
                stack=[]
        if i==s[-1]:
            if len(stack)>=k:
                print("Yes")
                flag=True
                break

    if flag==False:
        print("No")
