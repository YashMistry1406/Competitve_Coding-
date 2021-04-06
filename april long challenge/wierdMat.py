import collections

count=0
def mat(arr,k):
    c=collections.Counter()
    global count
    for i in arr:
        c.update(i)
    for key,value in c.items():
        if int(key)>=k:
            count+=value





if __name__=="__main__":
    for t in range(int(input())):
        n,m,k=map(int,input().split())
        stack=[[j for j in input().split()] for _ in range(n)]
        table={}
        table=mat(stack,k)
        print(sum(stack))
