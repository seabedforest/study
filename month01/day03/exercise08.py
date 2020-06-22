student_height_1 = float(input("输入身高："))
student_height_2 = float(input("输入身高："))
student_height_3 = float(input("输入身高："))
student_height_4 = float(input("输入身高："))
max = student_height_1
if max < student_height_2:
    max = student_height_2
if max < student_height_3:
    max = student_height_3
if max < student_height_4:
    max = student_height_4
print(max)
