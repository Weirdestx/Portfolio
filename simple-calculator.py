# Functions
# Functions to Add
def add(x, y):
  return x + y
# Functions to Subtract
def subtract(x, y):
  return x - y
# Functions to Multiply
def multiply(x, y):
  return x * y
# Functions to Divide
def divide(x, y):
  return x / y

# Showing the Calculator options
print("Welcome to my Calculator, please select an operation.")

while True:
  # Take input from the user
  next = 0
  print('')
  print("1. Add")
  print("2. Subtract")
  print("3. Multiply")
  print("4. Divide")
  print("5. Exit")
  print('')
  fchoice = input("Enter choice(1/2/3/4/5): ")

  # Check if choice is one of the four options
  if fchoice in ('1', '2', '3', '4'):
    try:
      num1 = float(input("Enter first number: "))
      num2 = float(input("Enter second number: "))
    except ValueError:
      print("Invalid input. Please enter a number only")
      continue

  
    # User has chosen Addiiton
    if fchoice == '1':
      print("")
      print(num1, "+", num2, "=", add(num1, num2))

    # User has chosen Subtraction
    elif fchoice == '2':
      print("")
      print(num1, "-", num2, "=", subtract(num1, num2))

    # User has chosen Multiplication
    elif fchoice == '3':
      print("")
      print(num1, "x", num2, "=", multiply(num1, num2))

    # User has chosen Division
    elif fchoice == '4':
      print('')
      if num1 == 0 or num2 == 0:
        print("Error: Cannot divide by 0")
        continue
      else:
        print(num1, "/", num2, "=", divide(num1, num2))

  
  # User has chosen to exit the calculator
  elif fchoice == '5':
    print("")
    print("Thank you for using my Calculator")
    break

  # User has chosen an invalid option
  else:
    print('')
    print('Invalid Input, please try again')
    continue