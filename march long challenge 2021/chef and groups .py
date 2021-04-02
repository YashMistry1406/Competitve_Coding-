"""""
def sumOfUnique(self, nums):
    uni=set()
    result=0
    for i in range(len(nums)):
        if nums[i] in uni:
            uni.remove(nums[i])
            result-=nums[i]
        else:
            uni.add(nums[i])
            result+=nums[i]
    if not uni:
        return 0
    else:
        return result
num=list(map(int,input().split()))
sumOfUnique(num)
"""

#d = [ map(str,raw_input().split()) for x in range(n)]
#dictonaries={1: 'yash',2:'mistry'}
#dictonaries.update(B='for')
#
#print(dictonaries)

#chef and groups code cehf march long challenge 2021
#
for k in range(int(input())):

    s=input()
    ls=list(s)
    print(ls)
    j=0
    stack=[]
    count=0
    for i in range(len(ls)):
        if ls[i]=='1':
            stack.append(ls[i])
        if ls[i]=='0' and stack:
            stack=[]
            count+=1
    if s[-1]=="1":
        count+=1
    print(count)

