for i in range(int(input())):
    n,k=map(int,input().split())

    if n==k:
        print(0)
        continue
    elif n<k:
        print(n)
        continue
    elif n%k ==0:
        print(0)
    else:

        print(n%k)

#    temp=n
#    while n>=0:
#        temp=n-k
#        if k> temp:
#            break
#        
#        else:
#            n=temp-k
#
#        
#    print(n)
