d = [{'item':'item1','amount':400},        # for i in d : i checks the items in the dictionary,
     {'item':'item2','amount':300},        # {'item':'item1','amount':400} these are the items in the dictionary
     {'item':'item1','amount':750}]

lst = {}  #empty dictionary
for i in d:
    if i['item'] not in lst:
        lst[i['item']]=i['amount']
    else:
        lst[i['item']]+=i['amount']
print(lst)
