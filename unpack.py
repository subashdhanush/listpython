list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
list3 = [True, 'hello', 3.14]
list4=[*list1,*list2]
print(list4)
list5=[*list1,*list3]
print(list5)
list6=[*list3,*list2]
print(list6)