# 1. String
greet = "Good Morning"
name = "Aman Raj"
print(greet+" "+name)   # concat
print(name[5])  # get character {can't set value}
print(name[0:4])    # slicing (forward)
print(name[-3:])    # slicing (backward)
print("Hi {0}, {1}!!!".format(name, greet)) # formatting functions
print(f"Hi {name}, {greet} :)") # format

# 2. Lists
arr = ["apple", "banana", "mango", 101, 102]
print(type(arr))    # type
print(len(arr))     # length
print(arr[2:4])     # slicing
arr.sort                # sort
arr.reverse             # reverse
arr.append(103)         # append
arr.insert(1,"kiwi")    # insert
for val in arr:
    print(val,end=" ")
print()

# 3. Tuples (immutable)
tup = ("maths", "physics", "chemistry", 95, 98, 100)
print(type(tup))    # type
print(len(tup))     # length
print(tup[2:4])     # slicing
print(tup.index("physics")) # index
print(tup.count(95))        # count

# 4. Dictionary
student = {
    "name": "aman",
    "cgpa": 9.09,
    "subjects": ["maths","physics"]
}
print(type(student))
print(student.get("name"))  # get
print(student.keys())       # keys
print(student.values())     # values
print(student.items())      # (key,value)
print(student.update({"status":"pass"}))#update
print(student)

# 5. Set
s = {1,2,2,3,3,3}
s.add(4)    # add
s.remove(2) # remove
s.pop()     # pop random value
s.clear()   # clear
s.union({7,8,9})        # union
s.intersection({8,9,10})# intersection
print(s)
