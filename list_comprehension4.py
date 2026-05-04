#1 Basic list comprehension

listcomp1 = [x for x in range(10)]
print(listcomp1)

#2 conditional list comprehension

listcomp2 = [x for x in range(10) if x%2 != 0]
print(listcomp2)

#3 If-else inside list comprehension
listcomp3 = ["even" if x %2 ==0 else "odd" for x in range(10)]
print(listcomp3)

## Nested List comprehension

#4 Matrix Flattening
matrix = [[4,5],[1,2],["Sunny","Shiwani"],["Gilchrist","Mayanti"]]

listcomp4 = [x for row in matrix for x in row]
print(listcomp4)

#5 Multiple Loops ( Cartesian Product)

pairs = [(x,y) for x in [1,2,3] for y in ["Anjali","Shiwani"]]
print(pairs)

#6 Real Data Cleaning Examples

raw_names=[]
emails=["SANNYMANANDHAR61@GMAIL.COM","ABRAHAMLINCOLN@HOTMAIL.COM"]
data=["SANNYMANANDHAR61@GMAIL.COM","ABRAHAMLINCOLN@HOTMAIL.COM",None]
# Real Data cleaning Examples
#Strip spaces
names = [name.strip() for name in raw_names]
#Lowercase normalization
emails1 = [email.lower() for email in emails]
print(emails1)
#Remove null values
clean = [x for x in data if x is not None]
print(data)
print(clean)
#These are very real production use cases.


#7 LIST COMPREHENSION WITH FUNCTIONS

def score(x):
    return x * 10
scores=[score(x) for x in range(5)]
print(scores)

#8 Dictionary + Object Extraction ( Production Level)
'''
#From API JSON
users = [user["name"] for user in api_response if user.get("active")]

#ML feature extraction
lengths = [len(text) for text in documents if text]
This is common in: - NLP pipelines - FastAPI responses - ETL jobs - analytics systems
'''

#9  Advanced Nested Conditions
values = [5,21,9]
result =[
    x*10 if  x > 10 else x+10
    for x in values
    if x is not None
]
print(result)

#10 Hard Interview Pattern

# Flattening 3D List

cube = [
[[1, 2], [3, 4]],
[[5, 6], [7, 8]]
]

fist=[num for rows in cube for b in rows for num in b]
print(fist)

# Conditional transformation pipeline

processed = [
x.strip().lower()
for x in texts
if isinstance(x, str) and x.strip()
]