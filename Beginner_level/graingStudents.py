def gradingStudents(grades):
    ret_grade = []
    for grade in grades:
        if grade < 38:
            ret_grade.append(grade)
        else:
            if grade % 5 == 0:
                ret_grade.append(grade)
            else:
                i = 0
                original = grade
                while grade % 5 != 0:
                    grade += 1
                    i += 1
                    if grade % 5 == 0 and i < 3:
                        ret_grade.append(grade)
                    elif grade % 5 == 0 and i >= 3:
                        ret_grade.append(original)
                
    return ret_grade

arr = [20, 35, 38, 58, 69, 70, 75, 90, 87]
print(arr)

res = gradingStudents(arr)
print(res)
