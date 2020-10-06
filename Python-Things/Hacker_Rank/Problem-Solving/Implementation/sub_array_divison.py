def sub_array_divison():
    n = int(input())
    numbers = list(map(int, input().split()))
    dates = list(map(int, input().split()))

    d = dates[0]
    m = dates[1]
    counter = 0
    for i in range(n):
        curr_sum = sum(numbers[i:i + m])
        if  curr_sum == d:
            counter += 1

    return counter

print(
    sub_array_divison()
)
