# Q1. Arithmetic Operations on Two Numbers

# Accept two integers from the user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Perform arithmetic operations
sum_result = num1 + num2
difference = num1 - num2
product = num1 * num2
division = num1 / num2 if num2 != 0 else "Undefined (division by zero)"

# Display results
print("Sum:", sum_result)
print("Difference:", difference)
print("Product:", product)
print("Division:", division)
