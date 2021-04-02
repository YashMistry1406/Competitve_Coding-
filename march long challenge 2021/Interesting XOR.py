def binary(n): #converting the list to a biary number 
    result = 0
    for digits in n:
        result = (result << 1) | digits
    return result
for t in range (int(input())):


    c=int(input())

    stack1=[]
    stack2=[]
    
    temp=list(map(int,bin(c).replace("0b","")))
    #print(temp)


    for i in range(len(temp)):

        if temp[i]==0:
            stack1.append(1)
            stack2.append(1)
        if temp[i]==1:
            if binary(stack1)>binary(stack2):#if stack1 value is greater than the stack2 we increment the stack2
                #and keep the stack1 same by making the next bit high

                stack2.append(1)
                stack1.append(0)
                continue
            if binary(stack2)>binary(stack1):

                stack1.append(1)
                stack2.append(0)
                continue
            if binary(stack1)==binary(stack2):
                stack1.append(1)
                stack2.append(0)
                continue
    result1= int("".join(str(i) for i in stack1),2)#converting a list to string to get the product of the number

    #print ("The value is : " + str(result1))
    result2= int("".join(str(i) for i in stack2),2)

    #print ("The value is : " + str(result2))
    print(result1*result2)








