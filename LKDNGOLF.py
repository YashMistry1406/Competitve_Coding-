for _ in range(int(input())):

    n,x,k=map(int,input().split())
    rem=(n+1)%k

    if x%k==0 or x%k==rem:
        print("YES")
    else:
        print("NO")




