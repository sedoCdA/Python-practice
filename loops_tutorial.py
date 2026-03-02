"""
Python Loops Tutorial
======================
This program teaches you how loops work in Python.
Loops allow you to execute a block of code multiple times.

There are two main types of loops in Python:
1. for loops - iterate over sequences
2. while loops - repeat while a condition is true
"""

# ============================================================================
# PART 1: FOR LOOPS
# ============================================================================

print("=" * 60)
print("PART 1: FOR LOOPS")
print("=" * 60)

# Example 1.1: Basic for loop with range()
print("\n1.1 - Basic for loop with range():")
print("Counting from 0 to 4:")
for i in range(5):
    print(f"  i = {i}")

# Example 1.2: For loop with custom start and stop
print("\n1.2 - For loop with custom start and stop:")
print("Counting from 2 to 7:")
for i in range(2, 8):
    print(f"  i = {i}")

# Example 1.3: For loop with step
print("\n1.3 - For loop with step (skip every 2nd number):")
print("Counting from 0 to 10 by 2s:")
for i in range(0, 11, 2):
    print(f"  i = {i}")

# Example 1.4: For loop iterating over a list
print("\n1.4 - For loop iterating over a list:")
fruits = ["apple", "banana", "orange", "grape"]
print("Fruits in the list:")
for fruit in fruits:
    print(f"  - {fruit}")

# Example 1.5: For loop with index using enumerate()
print("\n1.5 - For loop with index using enumerate():")
print("Fruits with their positions:")
for index, fruit in enumerate(fruits):
    print(f"  Position {index}: {fruit}")

# Example 1.6: For loop iterating over a string
print("\n1.6 - For loop iterating over a string:")
word = "Python"
print(f"Letters in '{word}':")
for letter in word:
    print(f"  {letter}")

# Example 1.7: Nested for loops
print("\n1.7 - Nested for loops (multiplication table):")
print("3x3 Multiplication table:")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"  {i} * {j} = {i * j}")

# Example 1.8: For loop with a dictionary
print("\n1.8 - For loop iterating over a dictionary:")
student_grades = {"Alice": 95, "Bob": 87, "Charlie": 92}
print("Student grades:")
for student, grade in student_grades.items():
    print(f"  {student}: {grade}%")

# ============================================================================
# PART 2: WHILE LOOPS
# ============================================================================

print("\n" + "=" * 60)
print("PART 2: WHILE LOOPS")
print("=" * 60)

# Example 2.1: Basic while loop
print("\n2.1 - Basic while loop:")
print("Counting from 0 to 4:")
count = 0
while count < 5:
    print(f"  count = {count}")
    count += 1  # Important: increment to avoid infinite loop!

# Example 2.2: While loop with user-like condition
print("\n2.2 - While loop with condition:")
print("Counting down from 5 to 1:")
countdown = 5
while countdown > 0:
    print(f"  {countdown}")
    countdown -= 1
print("  Blastoff!")

# Example 2.3: While loop with break statement
print("\n2.3 - While loop with break statement:")
print("Breaking out of loop when x equals 3:")
x = 0
while True:
    print(f"  x = {x}")
    if x == 3:
        print("  Breaking out of loop!")
        break
    x += 1

# Example 2.4: While loop with continue statement
print("\n2.4 - While loop with continue statement:")
print("Skipping when number is even:")
num = 0
while num < 6:
    num += 1
    if num % 2 == 0:
        print(f"  Skipping {num} (even)")
        continue
    print(f"  Processing {num} (odd)")

# ============================================================================
# PART 3: LOOP CONTROL STATEMENTS
# ============================================================================

print("\n" + "=" * 60)
print("PART 3: LOOP CONTROL STATEMENTS")
print("=" * 60)

# Example 3.1: break statement
print("\n3.1 - Break statement (exit loop early):")
print("Finding first number divisible by 7:")
for i in range(1, 20):
    if i % 7 == 0:
        print(f"  Found: {i}")
        break

# Example 3.2: continue statement
print("\n3.2 - Continue statement (skip to next iteration):")
print("Printing only odd numbers from 1 to 9:")
for i in range(1, 10):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(f"  {i}")

# Example 3.3: else clause with for loop
print("\n3.3 - Else clause with for loop:")
print("Searching for the number 5:")
numbers = [1, 2, 3, 4]
for num in numbers:
    if num == 5:
        print(f"  Found {num}!")
        break
else:
    print("  5 not found in the list")

# ============================================================================
# PART 4: PRACTICAL EXAMPLES
# ============================================================================

print("\n" + "=" * 60)
print("PART 4: PRACTICAL EXAMPLES")
print("=" * 60)

# Example 4.1: Sum of numbers
print("\n4.1 - Calculate sum of numbers 1 to 10:")
total = 0
for i in range(1, 11):
    total += i
print(f"  Sum: {total}")

# Example 4.2: Finding maximum value
print("\n4.2 - Find maximum value in a list:")
numbers = [45, 23, 89, 12, 56, 34]
max_value = numbers[0]
for num in numbers:
    if num > max_value:
        max_value = num
print(f"  List: {numbers}")
print(f"  Maximum: {max_value}")

# Example 4.3: Counting occurrences
print("\n4.3 - Count vowels in a string:")
text = "Hello World"
vowel_count = 0
for char in text.lower():
    if char in "aeiou":
        vowel_count += 1
print(f"  Text: '{text}'")
print(f"  Vowel count: {vowel_count}")

# Example 4.4: Creating a pattern
print("\n4.4 - Create a number pyramid:")
for i in range(1, 6):
    print("  " + "* " * i)

# ============================================================================
# PART 5: COMMON MISTAKES AND HOW TO AVOID THEM
# ============================================================================

print("\n" + "=" * 60)
print("PART 5: TIPS AND BEST PRACTICES")
print("=" * 60)

print("""
✓ BEST PRACTICES:
  1. Use 'for' loops when you know how many iterations you need
  2. Use 'while' loops when you have a condition to check
  3. Always update the loop variable in while loops (avoid infinite loops)
  4. Use 'break' to exit a loop early
  5. Use 'continue' to skip to the next iteration
  6. Use descriptive variable names (not just 'i', 'x', etc.)
  7. Indent your code correctly (4 spaces is standard in Python)

✗ MISTAKES TO AVOID:
  1. Infinite loops - forgetting to update the condition
  2. Off-by-one errors - using wrong range bounds
  3. Modifying loop lists while iterating
  4. Using wrong loop type for the task
  5. Forgetting to initialize variables before while loops
""")

print("=" * 60)
print("End of Loops Tutorial")
print("=" * 60)