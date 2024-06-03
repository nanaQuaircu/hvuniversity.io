def multiplication_table(number):
    print(f"Table of {number}:")
    for i in range(1,11):
        result = number*i
        print(f"{number} x {i} = {result}")

    
def addition_table(number):
    print(f"Table of {number}:")
    for i in range(1,11):
        result = number+i
        print(f"{number} + {i} = {result}")

def substraction_table(number):
    print(f"Table of {number}:")
    for i in range(1,11):
        result = number-i
        print(f"{number} - {i} = {result}")

def division_table(number):
    print(f"Table of {number}:")
    for i in range(1,11):
        result = number/i
        print(f"{number} / {i} = {result}")




print("----This application consists to enter a number first an after select an"
       "operator among a bunch of operator to perform a task----\n")
number = int(input("Enter a number: "))
print("Choose your preferred sign assigmnent among this below")
print("1.(x)")
print("2.(-)")
print("3.(+)")
print("4.(/)")
sign = int(input("Enter your sign number option: "))
if sign == 1:
   multiplication_table(number)
elif sign == 2:
    substraction_table(number)
elif sign == 3:
   addition_table(number)
elif sign == 4:
    division_table(number)


