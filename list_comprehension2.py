relist = [x**3 for x in range(10)]
print(relist)

# List comprehension  with if condition

relist2 = [x for x in range(10) if x%2==0]
print(relist2)

# List comprehension with complex expression

relist3 = [f"Number ::{x}" for x in range(5)]
print(relist3)