def kangaroo():
    info = list(map(int, input().split()))
    x1 = int(info[0])
    v1 = int(info[1])
    x2 = int(info[2])
    v2 = int(info[3])

    while True:
        test1 = x1 + v1
        test2 = x2 + v2
        if test1 == test2:
            print(test1, test2)
        x1 += v1
        x2 += v2

kangaroo()



