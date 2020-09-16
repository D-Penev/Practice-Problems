def list_elements_ratio():
    n = int(input())
    arr = list(map(int, input().split()))
    positiveElementsCount = get_all_positive_elements(arr)
    negativeElementsCount = get_all_negative_elements(arr)
    zeroElementsCount = get_all_zero_count_elements(arr)

    positiveRatio = positiveElementsCount / n
    negativeRatio = negativeElementsCount / n
    zeroRatio = zeroElementsCount / n

    print("{0:.6f}".format(positiveRatio))
    print(round(negativeRatio,6))
    print(round(zeroRatio,6))

def get_all_positive_elements(arr):
    return len(list(filter(lambda  x: x > 0, arr)))

def get_all_negative_elements(arr):
    return len(list(filter(lambda  x: x < 0, arr)))

def get_all_zero_count_elements(arr):
    return  len(list(filter(lambda x: x == 0, arr)))

list_elements_ratio()