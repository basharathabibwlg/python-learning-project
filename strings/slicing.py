b ="hello,world!"

print(b[2:5])

b = "Hello, World!"
print(b[:5])

b = "Hello, World!"
print(b[2:])


b = "Hello, World!"
print(b[-5:-2])

a = "Hello, World!"
print(a.upper())

a = "Hello, World!"
print(a.lower())


a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"


a = "Hello"
b = "World"
c = a + b
print(c)

a = "Hello"
b = "World"
c = a + " " + b
print(c)


age = 36
#This will produce an error:
txt = "My name is John, I am " + age
print(txt)

age = 36
txt = f"My name is John, I am {age}"
print(txt)


age = 36
txt = f"My name is John, I am {age}"
print(txt)

txt = f"The price is {20 * 59} dollars"
print(txt)


