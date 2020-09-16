def mini_max_sum():
    arr = list(map(int, input().split()))
    allSums = []

    for i in range(0, len(arr)):
        totalSum = 0
        if i == 0:
            totalSum = sum(arr[i + 1: len(arr)])
        elif i != 0:
            totalSum = sum(arr[i + 1: len(arr)])
            for index in range(0, i):
                totalSum += arr[index]
        allSums.append(totalSum)


    print(min(allSums), max(allSums))

mini_max_sum()