total_grades = int(input("Ingrese el total de notas: "))
grade_counter = 1
passed_grades_count = 0
failed_grades_count = 0
avg_passed_grades = 0
avg_failed_grades = 0
avg_total_grades = 0

while grade_counter <= total_grades:
    print(f"Ingrese la nota numero {grade_counter}")
    current_grade = int(input())
    if current_grade < 70:
        failed_grades_count += 1
        avg_failed_grades += current_grade
    else:
        passed_grades_count += 1
        avg_passed_grades += current_grade

    avg_total_grades += (current_grade/total_grades)
    grade_counter+=1

if failed_grades_count != 0:
    avg_failed_grades = avg_failed_grades/failed_grades_count
else:
    avg_failed_grades = 0

if passed_grades_count != 0:
    avg_passed_grades = avg_passed_grades/passed_grades_count
else:
    avg_passed_grades = 0

print (f"El estudiante tiene esta cantidad de notas aprobadas: {passed_grades_count}")
print (f"Este es el promedio de notas aprobadas: {avg_passed_grades}")

print (f"El estudiante tiene esta cantidad de notas desaprobadas: {failed_grades_count}")
print (f"Este es el promedio de notas desaprobadas: {avg_failed_grades}")

print (f"Este es el promedio total de notas: {avg_total_grades}")