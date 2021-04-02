for i in range(int(input())):
    d,c=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))


    asum=sum(a)
    bsum=sum(b)
    dd=2*d

    if asum>=150 and bsum>=150:
        if asum+bsum+dd > asum+bsum+c:
            print("YES")
        else:
            print("NO")
    if asum<150 and bsum>=150:
        if asum+bsum+dd+c>asum+bsum+dd+dd:
            print("YES")
        else:
            print("NO")
    if bsum<150 and asum>=150:
        if asum<150:
            if asum+bsum+dd+c>asum+bsum+dd+dd:
                print("YES")
            else:
                print("NO")


