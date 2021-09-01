nums = list(map(int,input().split()))
n= len(nums)
k = n - 2 
l = 0 
while(k >=0 ):
    if nums[k] < nums[k+1]:
        break 
    k-=1
l= n-1
if k < 0 :
    nums[::-1]
else:
    while(l > k ):
        if nums[l] > nums[k]:
            break
nums[k],nums[l]=nums[l],nums[k]
nums[k+1::-1]
print(nums)
