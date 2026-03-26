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