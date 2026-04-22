# File I/O
'''
    r - reading
    w - truncate & write
    x - create new & write
    a - append at end
    b - binary mode
    t - text mode
    + - open disk file for update(r&w)
''' 

# # Create new file - if file already exist then throws error
# f = open("etc/file.txt", "x")
# f.write("This is a file.\nCreated by Aman Raj.")
# f.close()

# # Append file
# f = open("etc/file.txt", "a")
# f.write("\nThank You")
# f.close()

# # Read file - pointer always moved to last read
# f = open("etc/file.txt", "r")
# print(f.read())
# f.close()

# # Write file - truncate first
# f = open("etc/file.txt", "w")
# f.write("Empty\nWrite")
# f.close()

# # Read-Write
# f = open("etc/file.txt", "r+")
# print(f.readline())
# f.write("Hello World")
# f.close()

# # with - auto close file
# with open("etc/file.txt", "r") as f:
#     print(len(f.read()))

# # delete
# import os
# os.remove("etc/file.txt")

# JSON
import json
json_str = '{"name":"Aman Raj", "age": 24, "graduated": true}'

# 1. loads, dumps - while working with strings
# loads - json to python dictionary
py_obj = json.loads(json_str)
print(type(py_obj), py_obj)

# dumps - python dictionary to json
py_obj = {
    "name": "Aman Raj",
    "age": 25,
    "subjects": ["Maths", "Physics"]
}
json_str = json.dumps(py_obj)
print(type(json_str), json_str)

# 2. load, dump - while working with files
with open("etc/profile.json", "r") as f:
    py_obj = json.load(f)
    print(type(py_obj), py_obj)

data = {
    "name": "Aman Raj",
    "age": 25,
    "subjects": ["Maths", "Physics"],
    "graduated": True
}
with open("etc/profile.json", "w") as f:
    json.dump(data,f, indent=4)