#Function

def funex(name, message):
    print(f"{name}! {message}")
funex("Radhey Patil", "Welcome to the Dypcet!\n")


def introduce(name, age):
    print(f"My name is {name}. I am {age} years old and I live in {city}.\n")

introduce(name="Radhey Patil",age=21)


def funex1(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

funex1("Radhey Patil")
print()


def funex2(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
funex2(Name="Radhey",Lastname="Patil", Age=21, Mobile=8745773265,)

#Example
a=int(input("Enter The First Number: "))
b=int(input("Enter the Second Number: "))

#Function for Addition
def addno(a,b):
    result=a+b
    return result
print("The Addition of two Numbers is: ",addno(a,b))

#Function for Subtraction
def subno(a,b):
    return a-b
print("The Subtraction of two Numbers is: ",subno(a,b))

#Function for Multiplication
def mulno(a,b):
    return a*b
print("The Multiplication of two Numbers is: ",mulno(a,b))

#Function for Division
def devno(a,b):
    return a/b
print("The Division of two Numbers is: ",devno(a,b))

#Lambda Function
a = int(input("Enter The First Number: "))
b = int(input("Enter the Second Number: "))


# Lambda function for Addition
addno = lambda a, b: a + b
print("The Addition of two Numbers is: ", addno(a, b))

# Lambda function for Subtraction
subno = lambda a, b: a - b
print("The Subtraction of two Numbers is: ", subno(a, b))

# Lambda function for Multiplication
mulno = lambda a, b: a * b
print("The Multiplication of two Numbers is: ", mulno(a, b))

# Lambda function for Division
devno = lambda a, b: a / b
print("The Division of two Numbers is: ", devno(a, b))
