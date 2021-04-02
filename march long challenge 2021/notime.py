n,h,x=map(int,input().split())

t=list(map(int,input().split()))
s=set(t)

if h-x in s:
    print("YES")
else:
    print("NO")



