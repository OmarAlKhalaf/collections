all_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
# All day's
print(all_days)
# Woking day's.
print(all_days[:5])
# Weekend day's.
print(all_days[5:])
# all day's revers.
all_days.reverse()
print(all_days)
#  working day's revers.
print(all_days[2:])
# weekend day's.
print(all_days[:2])

# Math list.
listOne = [1,2,3,4,5,6,7,8,9,10]
listTwo = [2,4,6,8,10,12,14,16,18,20]
# Plus list.
def math_plus ():
    global listOne,listTwo
    print('Plus list')
    for t in range(10):
        resultplus = listOne[t] + listTwo[t]
        print(f'{listOne[t]} + {listTwo[t]} = {resultplus}')
# Min list.
def math_min ():
    global listOne, listTwo
    print('Mix list')
    for q in range(10):
        result_min = listOne[q] - listTwo[q]
        print(f'{listOne[q]} - {listTwo[q]} = {result_min}')
# Multi list.
def math_multi ():
    print('Multi list')
    global listOne,listTwo
    for w in range(10):
        result_multi = listOne[w] * listTwo[w]
        print(f'{listOne[w]} x {listTwo[w]} = {result_multi}')
# Divided list.
def math_divided ():
    print('Divided list')
    global listOne,listTwo
    for e in range (10):
        result_divided = listOne[e] / listTwo[e]
        print(f'{listOne[e]} : {listTwo[e]} = {result_divided}')
print('*========================================*')
print('')
math_plus()
print('*========================================*')
math_min()
print('*========================================*')
math_multi()
print('*========================================*')
math_divided()
print('')
print('Iits Over :) ')