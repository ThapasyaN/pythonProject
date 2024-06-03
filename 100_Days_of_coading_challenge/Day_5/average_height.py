student_height = input().split()
for n in range(0, len(student_height)):
    student_height[n] = int(student_height[n])

total_height = 0
for height in student_height:
    total_height += height
print(f"total height = {total_height}")

num_students = 0
for students in student_height:
    num_students += 1
print(f"number of students = {num_students}")

average = round(total_height / num_students)
print(f"average height = {average}")

