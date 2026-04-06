# FOR LOOP

#Simple loop using range

for i in range(5):
    print(i)

#Loop through list
fruits = ["apple","banana","cherry","mango","pineapple"]
for a in fruits:
    print(a)

# Loop through String

for c in "Sunny":
    print(c)

# Loop through dictionary

ages={"Shiwani":25,"Anjali":35,"Pratima":22}
for name,age in ages.items():
    print(name,age)

# Loop with index
girlfriends=["Helen","Prajita","Poonam","Sushma","Arzoo"]

for i in range(len(girlfriends)):
    print(i,girlfriends[i])

# better option

for m,girlfriend in enumerate(girlfriends):
    print(m,girlfriend)

# WHILE LOOP in python

# Simple example

j=0

while j <= 5:
    print(j)
    j+=1

# Break statement with the implementation of infinite loop
print("# Break statement with the implementation of infinite loop")
i1=0

while True:
    print(i1)
    i1+=1
    if i1 == 7:
        break

# Continue statement with while loop
print("# Continue statement with while loop")
q=0
while q<10:

    q=q+1
    if q ==2:
        continue
    print(q)

# NESTED WHILE LOOP
l = "* "
mm=1
nn=1
while mm<3:
    mm+=1
    nn=1
    while nn<8:

        print(l*nn)
        nn += 1



# COMPLEX WHILE LOOP
'''
z = " "
f =  "*"
g=1
h=5

while g <=h:
    print(z*(h-g)+(f*g))
    g+=1
 '''
# SUPERCOMPLEX WHILE LOOP

z = " "
f =  "*"
g=1
h=5
ppt=0
while ppt < 2:
    while g <=h:
        print(z*(h-g)+(f*g)+f*(g-1))
        g+=1
    g=1
    ppt+=1