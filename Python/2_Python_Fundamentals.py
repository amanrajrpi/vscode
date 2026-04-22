# 1. Conditional Statements
# - if, elif, else
age = 18
if(age >=18):
    print("You are an adult")
elif(age>0):
    print("You are child")
else:
    print("Invalid age")

# 2. Match Case
color = "Red"
match color:
    case "Red":
        print("Stop")
    case "Yellow":
        print("Wait")
    case _:
        print("Go")

# 3. Loops
# - while
i = 1
while(i<=3):
    print("Hello World")
    i += 1

# - for
name = "aman raj"
for c in name:
    print(c,end=" ")

for i in range(0,2,1):
    print("\n",i)

# 4. Function
# - Types = Built-in, User-defined
def factorial(num): # Function defn
    if(num<=1):
        return 1
    num *= factorial(num-1)
    return num
print(factorial(5)) # Function call

# - Lambda Fn
avg = lambda a,b: (a+b)/2
print(avg(2,4))