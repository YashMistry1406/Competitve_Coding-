arr = list(map(int,input().split()))
minPrice = float('inf')
maxProfit=0
for value , index in enumerate(arr):

    minPrice = min(minPrice, value)
    maxProfit = max(maxProfit, value-minPrice)
print(maxProfit)