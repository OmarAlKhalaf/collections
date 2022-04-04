def Shopping_list ():
    global empty_list,item
    empty_list = list()
    print('Here onder you can add your shoping list ')
    item = input('Type here : ')
    if item == ''.lower:
        empty_list.extend(item)
    else:
        print('Sorry')
Shopping_list()
print(empty_list)
print(item)