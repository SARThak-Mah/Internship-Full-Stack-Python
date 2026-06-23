# Comparison Operators
a = 7
b = 18
c = 15

print(a == b)  # Output: False
print(a > b)   # Output: False
print(a < b)   # Output: True

# Logical Operators (Must be lowercase in Python)
print(a == b and c == b)  # Output: False
print(a > b and b > c)    # Output: False
print(a == b or b == c)   # Output: False
print(a < b and b > c)    # Output: True

# Membership Operators
lst = [5, 6, 7, 8]
print(5 in lst)       # Output: True
print(5 not in lst)   # Output: False

# Basic if-else
a = 3
b = 15
s = 18

if a == b:
    print("True block 1")
else:
    print("A == S")

# if-elif-else with logical 'or'
if a == s or s > b:
    print("True block 1")
elif a == s or b < s:
    print("True block 2")
else:
    print("else block")

# Nested if statements
a = 5
b = 10
c = 15

if a > b:
    print("A > B")
    if a > c:
        print("A > C")
    if a > c:
        print("A > B")
else:
    print("C > A")

# Dynamic addition with type casting
a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
c = a + b
print("result: ", c)

# Checking for Even or Odd numbers
a = int(input("Enter no: "))
if a % 2 == 0:
    print("Even")
else:
    print("odd")

# Finding the greatest among four numbers
a = 15
b = 18
c = 10
d = 20

if a > b and a > c and a > d:
    print("a is greatest")
elif b > a and b > c and b > d:
    print("b is greatest")
elif c > a and c > b and c > d:
    print("c is greatest")
else:
    print("D is greatest")

# While Loop with nested conditions
i = 1
while i <= 10:
    if i > 5:
        print(i)
    i = i + 1

# Multiplication Table sequence tracker
a = 15
j = 1
while j < 10:
    print(j * a)
    j += 1

print("--- For Loops ---")

# Step iterations using range(start, stop, step)
for i in range(1, 4, 1):
    print(i)  # Prints: 1, 2, 3

for i in range(1, 11, 2):
    print(i)  # Prints odd numbers: 1, 3, 5, 7, 9

# Negative step countdown
for i in range(10, 0, -1):
    print(i)  # Counts down: 10, 9, ..., 1

# Loop jumps using continue
for i in range(1, 11, 1):
    if i == 5:
        continue  # Skips printing 5 and jumps directly to 6
    print(i)