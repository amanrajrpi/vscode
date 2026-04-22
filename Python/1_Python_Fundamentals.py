# 1. Variables
# - Identifier = Value
# - Identifier can't start with number
name = "Aman"
age = 25
PI = 3.14
isPrime = True
x = None
print(name, age, PI, isPrime, x)

# 2. Operators
# - Arithmetic {+, -, *, /, %, **}
# - Relational {>, >=, ==, !=, <, <=}
# - Assignment {=, +=, -=, *=, /=, %=, **=}
# - Logical {not(), and, or}
print((5>3) and not(1<2))

# 3. Operator Precedence
# - If same then Left to Right
# - [()] > [**] > [*,/,%] > [+,-] > [==,!=,>,>=,<,<=] > not > and > or

# 4. Type Conversion
# - Implicit (done by own)
# - Explicit (casting done manually)
print(type(5+2.5))  #implicit
print(type(int("123"))) #explicit

# 5. Input
# - By default all inputs are taken as String
username = input("Enter username: ")
print("Welcome ",username)