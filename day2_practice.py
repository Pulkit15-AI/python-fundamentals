# Example-1 comparison operators
# print( 5 == 5) # equal to
# print( 5 != 3) # not equal to
# print( 7 > 3)  # greater than
# print( 7 < 3)  # less than
# print( 7 >= 7) # greater than or equal to
# print( 7 <= 3) # less than or equal to

# Example-2 a basic if
# age = 20
# if age >= 18:
#     print("You are an adult")

# Example-3 if/else
# age = 15
# if age >= 18:
#     print("You are an adult")
# else:
#     print("You are a minor")

# age = 20
# if age >= 18:
#     print("You are an adult")
# else:
#     print("You are a minor")

# Example-4 if/elif/else
# marks = 72
# if marks >= 90:
#     print("grade A")
# elif marks >= 75:
#     print("grade B")
# elif marks >= 50:
#     print("grade C")
# else:
#     print("fail")        

# marks = 95
# if marks >= 90:
#     print("grade A")
# elif marks >= 75:
#     print("grade B")
# elif marks >= 50:
#     print("grade C")
# else:
#     print("fail")

# marks = 80
# if marks >= 90:
#     print("grade A")
# elif marks >= 75:
#     print("grade B")
# elif marks >= 50:
#     print("grade C")
# else:
#     print("fail") 

# marks = 30
# if marks >= 90:
#     print("grade A")
# elif marks >= 75:
#     print("grade B")
# elif marks >= 50:
#     print("grade C")
# else:
#     print("fail") 

# Example-5 use input
# age = int(input("enter your age: "))
# if age >= 30:
#     print("you are already 30 or older")
# else:
#     print(f"you will be 30 in {30 - age} years")
         
# Error 1
# age = 20
# if age > 18 # expected ':'
#  print("You are an adult")

# Error 2
# age = 18
# if age >= 18: # expected an indentation block after ;if statement on line 82
# print("You are an adult")

# Error 3
# age = 18
# if age = 18: # invalid syntax maybe you meant '==' or ':=' instead of '='?
#     print("you are an adult")


#------loops
# Example-1 a while loop
# count = 1
# while count <= 5:
#     print(count)
#     count = count + 1
# print("done")

# Example-2 a loop that never ends
# count = 1 
# while count <= 5:
#     print(count)

# Example-3 a for loop with range()
# for i in range(5):
#     print(i)

# Example-4 choose start and end
# for i in range(1,6):
#     print(i)

# Example 5 loop wuith a step
# for i in range(2,11,2):
#     print(i)
# Example-6 breaks stops the loop
# while True:
#     answer = input("type 'quit' to stop: ")
#     if answer == 'quit':
#         break
#     print(f"You typed: {answer}")
# print("loop ended")

# Example-7 continue skips one round
for i in range(1,11):
    if i % 2 == 0:
        continue
    print(i)
