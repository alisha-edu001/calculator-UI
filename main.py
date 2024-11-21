from addition import add
from subtraction import subtract
from Multiplication import multiply
from division import divide

def calculator ():

    while True:
         num1 =float (input("enter the number"))
         num2 = float (input("enter the number"))
         operator= input("enter the operator(+,-,*,/)")
         if operator == "+":
             result = add(num1, num2)
         elif operator == "-":
             result = subtract(num1, num2)
         elif operator == "*":
             result = multiply(num1, num2)
         elif operator == "/":
             result = divide(num1, num2)
         else:
            print ("wrong operator.Try again:")
            continue
         print(f"The result is: {result}")
         quit_calculator =input("Do you want to quit??(Y/N)").strip().lower()
         if quit_calculator=="y":
            break
         else:
                continue
calculator ()