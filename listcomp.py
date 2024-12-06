list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

# merge two lists using list comprehension
list3 = [item for lists in [list1, list2] for item in lists]
print(list3)