#Simple Calculator program

name = input("Enter your name: ")

print(f"Hello {name}, welcome to a simple calculator program. You can do addition, subtraction, multiplication, and division in this calculator.")

print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division")

operator = int(input("What to you want to do? (1, 2, 3, 4)"))
digit1 = float(input("Enter the first digit: "))
digit2 = float(input("Enter the second digit: "))

addition = digit1 + digit2
subtraction = digit1 - digit2
multiplication = digit1 * digit2
division = digit1 / digit2

if operator == 1:
  print(addition)
elif operator == 2:
  print(subtraction)
elif operator == 3:
  print(multiplication)
elif operator == 4:
  print(division)
else:
  print(f"{operator} is not a valid operator.")