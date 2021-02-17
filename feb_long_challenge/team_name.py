"""
for j in range(int(input())):


    n= int(input())
    stack = [item for item in input().split()]
    first=set()
    for i in range(len(stack)):
        if stack[i][0] in first:
            continue
        else:
            first.add(stack[i][0])
    print(first)
    if len(first)==1:
        print(0)
    else:
        print(len(first))
"""

from collections import Counter




for _ in range(int(input())):


































