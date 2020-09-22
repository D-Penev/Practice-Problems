def information_about_speed():
    speed = float(input())

    if speed <= 10:
        return 'slow'
    elif  speed > 10 and speed <= 50:
        return  'average'
    elif speed > 50 and speed <= 150:
        return  'fast'
    elif speed > 150 and speed <= 1000:
        return 'ultra fast'
    else:
        return 'extremely fast'

print(
    information_about_speed()
)