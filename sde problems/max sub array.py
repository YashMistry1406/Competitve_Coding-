# Kadane Algo
stack= list(map(int,input().split()))
sum_ = 0 
maxi = float('-inf')
for i in range(len(stack)):
    sum_ += stack[i]
    maxi= max(sum_, maxi)
    if sum_ < 0 :
        sum_ = 0 

print(maxi)