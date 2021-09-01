'''
1)Here we take the last element of the first row and then traverse through the array 
2)if the current element in the array is bigger than the target value we move down in the array and if it is smaller than the target we move to left of the matrix 
3)when found print true 

n = int(input())
target = int(input())
arr = [[int(input()) for _ in range(n)] for k in range(n)]

i = 0 
j = n-1
flag = False 
while(i < n and j>=0):
    if arr[i][j] == target:
        flag = True 
    if arr[i][j] > target:
        j-=1
    else:
        i+=1
if flag == True:
    print(True)
else:
    print(False)
'''



def solve(arr,n,target):
    if len(arr)==0:
        return False
    n = len(arr)
    m = len(arr[0])

    lo = 0 
    hi = (n*m)-1
    mid = 0 

    while(lo <= hi ):
        mid = (lo + (hi - lo))//2
        if arr[int(mid/m)][int(mid % m)] == target:
            return True 
        elif arr[int(mid/m)][int(mid % m)] < target :
            lo = mid + 1
        else:
            hi = mid -1 
    return False 
n = int(input())
target = int(input())
arr = [[int(input()) for _ in range(n)] for k in range(n)]

solve(arr,n , target)
