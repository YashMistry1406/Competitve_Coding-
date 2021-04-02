for t in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    cost=0
    last=[]

    for i in range(len(l)-1):
        temp=l[i:]
        #print("temp",temp)


        mini=min(temp)
        #print("mini",mini)


        j=l.index(mini)
        #print("j",j)


        l=l[:i]+l[i:j+1][::-1]+l[j+1:]
        #print("l",l)
        cost+=j-i+1
        #print("cost",cost)
    print(f"Case #{t+1}: {cost}")




