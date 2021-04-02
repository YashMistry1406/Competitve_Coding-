for t in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    arr.sort()
    diff=0

    flag=0
    for i in range(n):
        if arr[i]>i+1:
            flag=1
        else:
            diff+=i+1-arr[i]
    if flag==0:
        if diff and 1:
            print("First")
        else:
            print("Second")

