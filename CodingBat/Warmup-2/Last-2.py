def last_2(str):
    if(len(str) < 2):
        return 0

    lastTwoElements = str[len(str) - 2:]
    counter = 0

    for i in range(len(str) - 2):
        currentSubstring = str[i : i + 2]
        if currentSubstring == lastTwoElements:
           counter+=1

    return counter