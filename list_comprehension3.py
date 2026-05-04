 # list comprehension

list1 = [x for x in range(10)]
print(list1)

# Conditional list comprehension

list2 = [x for x in range(10) if x%2 == 0]
print(list2)

# ifelse inside list comprehension

list3 = ["even" if x%2 == 0 else "odd" for x in range(10)]
print(list3)