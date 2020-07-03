'Write a program that serves as a basic calculator.'
'It asks for two numbers, then it asks for an operator.'
'Gracefully deal with input that doesnt cleanly convert to numbers.'
'Deal with division by zero errors.'

x = float(input("Enter first number :"))
y = float(input("Enter second number :"))

print("1 Add the two numbers")
print("2 Subtract the two numbers")
print("3 Multiply the two numbers")
print("4 Divide the two numbers")

choice = int(input("Enter your choice :"))

print("The calculation of first and second number is :", end="")

try:
   if choice == 1:
      print(x+y)
   elif choice == 2:
      print(x-y)
   elif choice == 3:
      print(x*y)
   elif choice == 4:
      print(x/y)
   else:
      print("You did not enter a valid choice.")

except ZeroDivisionError:
    print("Division by zero is not allowed.")
    print("Please enter a non-zero number.")
print("Code after the exception.")