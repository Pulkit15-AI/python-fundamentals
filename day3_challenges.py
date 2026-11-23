#----challenge 1: square----
# def square(a):
#     return a * a

# number = square(-3)
# print(number)

#----challenge 2:is_even----
# def is_even(a):
#     if a % 2 == 0:
#         return "True"
#     else:
#         return "False"

# test = is_even(10)
# print(test)

#----challenge 3:max of three----
# def max_of_three(a,b,c):
#     if a >= b and a >=c:
#         return a
#     elif b >= a and b >= c:
#         return b
#     else:
#         return c

# result = max_of_three(3,9,5)
# print(result)

# result =  max_of_three(5,5,9)
# print(result)

#----challenge 4: grade----
# def grade(marks):
#     if marks >= 90:
#         return "A"
#     elif 89 >= marks >= 75:
#         return "B"
#     elif 74>= marks >= 50:
#         return "C"
#     else:
#         return "fail"

# result = grade(95)
# print(result)

# result = grade(49)
# print(result)

# result = grade(75)
# print(result)

#----challenge 5:total----
# def total(n):
#     sum = 0
#     for i in range(1,n + 1):
#         sum = sum + i
#     return sum 

# answer = total(5)
# print(answer)

# answer = total(10)
# print(answer)

#----challenge 6: table----
def table(n):
    for i in range(1,11):
        print(f"{n} X {i} = {n * i}")

table(7)

