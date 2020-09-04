def intro_four():
    uselessData = list(map(int, input().split()))
    arr =  set(map(int, input().split()))
    a = set(map(int, input().split()))
    b = set(map(int, input().split()))
    totalHappiness = 0
    for i in range(len(arr)):
        isInA = i in a
        isInB = i in b
        if isInA:
            totalHappiness+=1
        elif isInB:
            totalHappiness-=1
    return totalHappiness

print(
    intro_four()
)
    