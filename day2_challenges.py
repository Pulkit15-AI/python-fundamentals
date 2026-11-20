#---challenge 1: count down from 10 to 1 ---
# for i in range(10,0,-1):
#     print(i)

#---challenge 2: multiplicationof 5 ---
# for i in range(1,11):
#     print(f"5 x {i} = { i * 5}")

#---challenge 3: sum from 1 to a number ---
num = int(input("Enter your number: "))
total = 0
for i in range(1,num + 1):
    total = total + i 
print(total)    
