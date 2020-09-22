def bonus_points():
    number = int(input())
    bonus = 0

    if number <= 100:
        bonus += 5
    elif number > 100 and number <= 1000:
        bonus += ((number * 20) / 100)
    else:
        bonus += ((number * 10)/ 100)

    if number % 2 == 0:
        bonus += 1

    test = number % 10


    if test == 5:
        bonus += 2

    print(bonus)
    print(number + bonus)

bonus_points()