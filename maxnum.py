# Maximum of two numbers in Python
# Given two numbers, write a Python code to find the Maximum of these two numbers.

# Method-1__________Method-1

# enter first number
num1=int(input('enter first number :'))

# enter secound number
num2=int(input('enter second number :'))

# calculation
if num1>num2:
    print(num1)
else:
    print(num2)   

  
#Method-2___________Method-2

# here we use max() function

# enter the value of a
a=int(input("Enter the value of a: "))

# enter the value of b
b=int(input("Enter the value of b: "))

# max function
maximum=max(a,b)

# output
print("Maximum number is :",maximum)
