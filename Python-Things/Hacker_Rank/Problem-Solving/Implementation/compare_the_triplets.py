a = list(map(int, input().split()))
b = list(map(int, input().split()))
alicePoints = 0
bobPoints = 0
for i in range(0, len(a)):
    if a[i] > b[i]:
        alicePoints += 1
    elif b[i] > a[i]:
        bobPoints += 1

print(alicePoints, bobPoints)