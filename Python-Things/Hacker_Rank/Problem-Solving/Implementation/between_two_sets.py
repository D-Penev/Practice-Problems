def between_two_sets():
    arr_sizes = list(map(int, input().split()))
    arr_one = list(map(int, input().split()))
    arr_two = list(map(int, input().split()))
    totalCounter = _get_factor(arr_one, arr_two)

def _get_factor(arr1, arr2):
    counter = 0
    for i in range(0,len(arr1)):
        counter += are_all_elements_factor_firstArr(arr1)
        counter += are_all_elements_factor_firstArr(arr2)

def are_all_elements_factor_firstArr(arr1, curr_value):
    factorCounter = 0
    for i in range(0, len(arr1)):
        if i % curr_value   == 0:
            factorCounter+=1





def _are_all_elements_factor_secondArr(arr2, curr_value):
    factorCounter = 0
    for i in range(0, len(arr2)):
        if i % curr_value == 0:
            factorCounter += 1
