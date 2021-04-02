for t in range(int(input())):

    w1,w2,x1,x2,m=map(int,input().split())

    l1=x1*m
    l2=x2*m
    diff=w2-w1

    if diff>= l1 and diff <=l2:
        print(1)
    else:
        print(0)
