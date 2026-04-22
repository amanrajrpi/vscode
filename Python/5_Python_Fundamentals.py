# Exception Handling

try:
    x = int(input("Enter x: "))
    ans = 10/x

except ValueError:
    print("Invalid input")

except ZeroDivisionError:
    print("Can't divide by zero")

else:   # if try run successfully
    print(f"Answer is: {ans}")

finally:
    print("End of Program")

# List comprehensions
sq_list = [i*i for i in range(6)]
print(sq_list)