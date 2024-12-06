from itertools import chain

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

# using chain() function
list3 = list(chain(list1, list2))
print(list3)