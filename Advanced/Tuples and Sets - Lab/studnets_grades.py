#2. Students' Grades

#Write a program that reads students' names and their grades and adds them to the student record.

#On the first line, you will receive the number of students – N. 
#On the following N lines, you will be receiving a student's name and grade. 
#For each student print all his/her grades and finally his/her average grade, formatted to the second decimal point in the format: "{student's name} -> {grade1} {grade2} ... {gradeN} (avg: {average_grade})".
#The order in which we print the result does not matter.

n = int(input())
students_data = {}

for _ in range(n):
    student_name, grade = input().split(' ')
    if student_name not in students_data:
        students_data[student_name] = []

    students_data[student_name].append(float(grade))

for student, grades in students_data.items():
    convert_grades_to_string = ' '.join(map(lambda grade: f'{grade:.2f}', grades))
    average_grade = sum(grades) / len(grades)
    print(f'{student} -> {convert_grades_to_string} (avg: {average_grade:.2f})')
