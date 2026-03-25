# IF STATEMENT

x=2

if x< 5:
    print(f"{x} is less than 5")
elif x==5:
    print(f"{x} is equal to 5")
else:
    print(f"{x} is greater than 5")

# NESTED IF
y=9
if x<5:
    if y>10:
        print("x is less than 5 and y is greater than 10")

# CONDITIONAL EXPRESSION ( TERNARY OPERATOR)

p=16
message="greater than 10" if p>10 else "less than 10"

print(message)

# TERNARY OPERATOR WITH LOGICAL OPERATOR

isWeekend = False
isHoliday = False
activity = "Relax" if (("Sleep" if isWeekend else "Work")== "Sleep" or isHoliday) else "Run"
print(activity)