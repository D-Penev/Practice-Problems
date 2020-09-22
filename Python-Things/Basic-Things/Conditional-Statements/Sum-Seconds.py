import math

def sum_seconds():
    timeOfFirst = int(input())
    timeOfSecond = int(input())
    timeOfThird = int(input())
    totalTime = timeOfThird + timeOfSecond + timeOfFirst

    total_minutes = totalTime / 60
    total_seconds = totalTime % 60
    total_minutes = math.floor(total_minutes)
    if total_seconds < 10:
        return f'{total_minutes}:0{total_seconds}'
    else:
        return f'{total_minutes}:{total_seconds}'


print(sum_seconds())