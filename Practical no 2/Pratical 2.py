n = int(input("Enter the number:"))
for x in range(0, n):
    if x % 2 == 0:
        print(x)

sum = 0
for x in range(0, n):
    if x % 2 == 0:
        sum += x

print("sum of even = ", sum)

#factorial
n = int(input("Enter the number:"))
fact = 1
for x in range(1, n + 1):
    fact *= x
print(fact)

#Reverse
n = "number"
print(f'Reverse: {n[::-1]}')

#Palindrome
a = input("Enter :")
b = ""
for x in a[-1::-1]:
    b+=x

print("Palindrome = "+b)

if b == a:
    print(f"{a} is a palindrome")

else:
    print("not a palindrome")

#Prime
n = int(input("Enter the number:"))
count =0
for x in range (1,n+1):
    if n % x == 0:
        count += 1
        sum = n
if count == 2:
    print("Given number is a prime number")
    print(sum)
else:
    print("not a prime")

