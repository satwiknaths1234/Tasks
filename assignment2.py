#task1 

num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is an even number.")
else:
    print(f"{num} is an odd number.")       

#task2

total = 0
for i in range(1, 51):
    total = total + i
print(f"The sum of numbers from 1 to 50 is: {total}")
    