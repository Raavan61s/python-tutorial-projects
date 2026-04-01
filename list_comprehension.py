numbers = [1,2,3,4,5,6,7,8,9,10]
fruits = ["apple","orange","grapes","banana","kiwi","dragondruit"]
mixed=[4,"Shiwani",99.9,"Anjali",True,"Priya"]


# List Comprehension

squares = [x**2 for x in range(11)]
print(squares)


# filtering even numbers using list comprehension

even_numbers = [n for n in numbers if n % 2==0]
print(even_numbers)


# Complex Expressions
formatted = [f"Number : {x}" for x in numbers]
print(formatted)