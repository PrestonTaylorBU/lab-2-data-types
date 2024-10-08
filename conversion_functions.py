# Create variables x, y, z, where x is a string, y is an integer and z is a float.
x = "Yo."
y = 727
z = 262.262

# 1) Find the data type of x. <class 'str'>
print(type(x))

# 2) Find the data type of y. <class 'int'>
print(type(y))

# 3) Find the data type of z. <class 'float'>
print(type(z))

# 4) Find the result and data type of y + z. Result: 989.262 Type: <class 'float'>
result = y + z
print(f"Result: {result} Type: {type(result)}")

# 5) Find the result and data type of y + int(z). Result: 989 Type: <class 'int'>
result = y + int(z)
print(f"Result: {result} Type: {type(result)}")

# 6) Find the result and data type of z + float(y). Result: 989.262 Type: <class 'float'>
result = z + float(y)
print(f"Result: {result} Type: {type(result)}")

# 7) Find the data type of str(z). <class 'str'>
print(type(str(z)))

# 8) Find the result and data type of x + str(y) + str(z). Result: "Yo.727262.262" Type: <class 'str'>
result = x + str(y) + str(z)
print(f"Result: {result} Type: {type(result)}")

# 9) Can we add x + y? No. Will throw a TypeError as you can only concatenate strs to other strs.
# print(x + y)