def college():
    #TODO
    pass
for t in range(int(input())):
    n,e,h,a,b,c=map(int,input().split())
    price={'a':a,'b':b,'c':c}
    indi={'e':e,'h':h}
    sorted_dict = {}
    sorted_keys = sorted(price, key=price.get)

    for w in sorted_keys:
        sorted_dict[w] = price[w]
    print(sorted_dict)
    item=0
    res=0
    bill=0
    temp_item=0
    for i in sorted_dict:
        if i =='a':
            temp_item=indi['e']//2
            indi['e']=indi['e']-temp_item
            item+=temp_item
            bill+=temp_item*price['a']
        if i=='b':
            temp_item+=indi['h']//3
            indi['h']=indi['h']-temp_item
            item+=temp_item
            print(indi)

            bill+=temp_item*price['b']

        if i=='c':
            '''
            temp = min(indi.values()) 
            res = [key for key in indi if indi[key] == temp] 
            item+=int(str(res))
            '''
            values=indi.values()
            print(values)
            item+=min(values)

            bill+=item*price['c']
    print(bill)


























    '''

    temp = min(price.values())
    for i in price:
        if price[i]==temp:
            res=i
    if res=='a':
        while  e>0 and e>1:
            temp_item+=1
            e-=2
        bill=price['a']*temp_item
        item=temp_item
    print(bill)
'''


