for t in range(int(input())):
    
    n,m,k=map(int,input().split())
    
    stack=[[k]*n]*m
    
    for i in range(len(stack)):
        for j in range(len(stack)):
            stack[i]+=stack[i]+i+j
            
    xor=0
    for k in stack:
        xor=xor^k
    print(xor)
    
