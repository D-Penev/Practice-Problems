def grading_students():
    n = int(input())
    for i in range(0, n):
        currentGrade = int(input())
        if currentGrade >= 38:
            for grade in range(currentGrade, 101):
                if grade % 5 == 0 and grade - currentGrade < 3:
                    currentGrade = grade
        print(currentGrade)

grading_students()
