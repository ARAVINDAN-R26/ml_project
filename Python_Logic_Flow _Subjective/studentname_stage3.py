#Stage 3: Student Grade Calculator

# Task: Calculate student grade based on marks in 3 subjects.

# Input: Student name, 3 subject marks (0-100)

# Calculate:

# Total marks
# Percentage = (total/300) * 100
# Grade Logic:

# A: >= 75%
# B: >= 60%
# C: >= 40%
# F: < 40%


name = input("Enter the name of the student: ")

print("Enter 3 subject marks between 0 to 100: ")
mark1 = int(input())
mark2 = int(input())
mark3 = int(input())

total_mark = mark1 + mark2 + mark3
print("Total: ", total_mark,"/300")
percentage = (total_mark / 300) * 100
print("Percentage: ", percentage, "%")

if percentage >= 75:
    print("Grade: A")
elif percentage >= 60:
    print("Grade: B")
elif percentage >= 40:
    print("Grade: C")
elif percentage < 40:
    print("Grade: F")

