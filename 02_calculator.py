def add(num1,num2):
    return num1+num2

def multiply(num1,num2):
    return num1*num2

def divison(num1,num2):
    return num1/num2

def substraction(num1,num2):
    return num1-num2

print("Select the operation:-\n"\
      "1.Add\n"\
      "2.Substract\n"\
      "3.Multiply\n"\
      "4.Divide\n")
select = int(input("Select operation from 1,2,3,4: "))
number1 = int(input("Enter the first number:"))
number2 = int(input("Enter the second number :"))

if select == 1:
    print(f'{number1}+{number2}={add(number1,number2)}')
elif select == 2:
    print(f'{number1}-{number2}={substraction(number1,number2)}')
elif select == 3:
    print(f'{number1}x{number2}={multiply(number1,number2)}')
elif select == 4:
    print(f'{number1}/{number2}={divison(number1,number2)}')
else:
    print("Invalid Choice")
