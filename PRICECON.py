for T in range(int(input())):
    N,K=map(int,input().split())
    P=list(map(int,input().split()))
    add=0
    for i in P:
        if i>K:
            add+=i-K
    print(add)
