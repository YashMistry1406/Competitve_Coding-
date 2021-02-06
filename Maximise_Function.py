def partition(arr,low,high):
    i = ( low-1 )         # index of smaller element 
    pivot = arr[high]     # pivot 
    for j in range(low , high): 
        if   arr[j] < pivot: 
            i = i+1
            arr[i],arr[j] = arr[j],arr[i] 
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 )
def quickSort(arr,low,high): 
    if low < high: 
        pi = partition(arr,low,high) 
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high) 


for i in range(int(input())):
    temp=int(input())
    S=list(map(int,input().split()))

    n=len(S)
    quickSort(S,0,n-1)
    mid=n//2
    x=S[0]
    y=S[mid]
    z=S[n-1]
    print(abs(x-y)+abs(y-z)+abs(z-x))
