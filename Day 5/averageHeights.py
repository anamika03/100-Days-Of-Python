student_height = input().split()
for n in range(0, len(student_height)):
    student_height[n] = int(student_height[n])
total_height = 0
for height in student_height:
    total_height += height
print(f"total height = {total_height}")
num_student = len(student_height)
print(f"number of students = {num_student}")

ave_height = total_height / num_student
print(f"average height of the {num_student} students is {int(ave_height)}")