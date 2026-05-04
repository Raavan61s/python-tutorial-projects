# Basic list comprehension

relist = [x for x in range(10)]
print(relist)

relist2 = [x**2 for x in range(10)]
print(relist2)

# Conditional list comprehension

relist3 =[x for x in range(10) if x%2!=0]
print(relist3)

# If else inside list comprehension

relist4=["even" if x%2 ==0 else "odd" for x in range(10)]
print(relist4)

# Nested list comprehension

#Matrix flattening

matrix =[[1,2],[3,4],[5,6],[7,8]]
relist5 =[x for row in matrix for x in row]
print(relist5)

# So this is the basic explanation of how things work inside matrix flattening

relist6=[]

for a in matrix:
    for b in a:
        relist6.append(b)

print(relist6)

# Multiple loops (Cartesian Product)

relist7 = [(m,n) for m in [4,5,6] for n in ['a','b']]
print(relist7)

relist8=[]
for p in [2,3,4]:
    for q in ['san','man']:
        relist8.append((p,q))

print(relist8)

# Real Data Cleaning examples
names=["SANNY"," ","SHIWANI","ANJALI","POONAM"," ","DIKSHYA"]

relist10=[x.lower() for x in names if x is not None]
print(relist10)

# List comprehension using function

def product(xx):
    return xx * 10

relist11 =[product(xx) for xx in range(6)]
print(relist11)