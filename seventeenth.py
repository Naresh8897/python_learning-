def add (x,y):
    return x+y
def substraction (x,y):
    return x-y
def multiplication (x,y):
    return x*y
while True:
    choice = input("enter choice: ")
    for choice in (1,4):
        num1 = int(input("enter number 1:"))
        num2 = int(input("enter number 2:"))
        if choice == 1:
            print(add(num1, num2))
        elif choice == 2:
            print(substraction(num1, num2))
        elif choice == 3:
            print (multiplication(num1, num2))
            break
        else:
            print("input is wrong")
