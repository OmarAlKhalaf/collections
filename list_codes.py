
# my list same .
list_name =[1,2,3,4,5,6]

# 1 to add somthing to the end of the list.
list_name.append()
# 2 to add somthing to the list where ever u want.
list_name.insert(0,)
# 3 to add multipel values individully to the list.
list_name.extend()
# 4 to remove somthing from the list
list_name.remove(1)
# 5 to remove the last thing from the list & we can git it back if we want.
list_name.pop()
popped = list_name.pop()
# 6 to reverse it 
list_name.reverse()
# 7 to sort it in alphabetical or alphanumeric
list_name.sort()
list_name.sort(reverse=True)#u can do that too..
sorted_list_name = sorted(list_name)# u can do this with out change anthing in the list.
# 8 min/max and sum {u can add it with print like this }
print(sum(list_name))
# 9 if u want to know if u want 'anme ' anything in ur list u can use .
print('name' in list_name)
# 10 u can use for loop with the list.
for item in list_name:
    print(item)
for index, item in enumerate (list_name, start=1):
    print(index, item)
# 11 join u can add somthing like this ', ' + u can change it to str.
join_str = ', '.join(list_name)
print(join_str)
# 12 here u can make a str back to a list like this .
new_join_list = join_str.split(' - ')
print(new_join_list)
# 13 sets {} is the same as list but it uotput randome values and they use this one {} like this
sets = {'anything','anything','anything','anything','anything'}
print(sets)
# 14 if u want to know if u have 2 sets and they have the same input the u can sue this to check it 
sets_2 = {'anything','anything','anything','anything','anything'}
print(sets.intersection(sets_2))
# 15 or the differences on it then u can do this 
print(sets.difference(sets_2))
# 16 if u want to combine 2 diferenc sets u can use this 
print(sets.union(sets_2))
# 17 hot to make a empty list / tuple and sets 
empty_list = []
# or 
empty_list = list()
empty_tuple = ()
empty_tuple = tuple()
empty_set = set() # here u can't use this empty_set = {} that is not a way to make a set in this wayt u make dictionary.
