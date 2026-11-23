#---Example-1-----
# def say_hello():
#     print("hello!")

# say_hello()
# say_hello()

#---Example-2-----
# def greet(name):
#     print(f"Hello {name}, you're going to be an ML eningeer ")

# greet("Pulkit")
# greet("Oscar")

#---Example-3-----
# def add(a, b):
#     print(a+b)

# add(7,8)
# add(20,7)

#---Example-4-----
# def add(a, b):
#     return a + b

# result = add(3,4)
# print(result)
# print(add(10,25) * 2)

#---Example-5-----
# def greet(name = "Friend"):
#     print(f"hello {name}")

# greet()
# greet("Pulkit")

#---Example-6-----
# def grade(marks):
#     if marks >= 90:
#         return "A"
#     elif marks >= 75:
#         return "B"
#     elif marks >= 60:
#         return "C"
#     else:
#         return "Fail"

# print(grade(95))
# print(grade(72))
# print(grade(30))

#---Example-7-----
# def make_message():
#     message = "Created inside the fucntion"
#     print(message)

# make_message()
# print(message) # name ' message' is not defined

#--Error:1---
# def add(a, b):
#     print(a + b)

# add(3,) # error required argument 'b'

#--Error:2---
# hello() # name hello is not defined

#--Error:3---
def greet(name)
    print(f"Hello {name}")

greet("Pulkit")
