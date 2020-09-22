def time_plus_15_mins():
    hours = int(input())
    minutes =int(input())

    remainder_of_minutes = 0
    if minutes + 15 >= 60:
        remainder_of_minutes = (minutes + 15) % 60
        minutes = remainder_of_minutes
        if hours == 23:
            hours = 0
        else:
            hours += 1
    else:
        minutes += 15

    if minutes < 10:
        print(f'{hours}:0{minutes}')
    else:
        print(f'{hours}:{minutes}')


time_plus_15_mins()