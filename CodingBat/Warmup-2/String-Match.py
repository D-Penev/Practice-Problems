  
def string_match(a,b):
    counter = 0
    for i,j in zip(range(len(a)), range(len(b))):
        sequenceOne = a[i: i + 2]
        sequenceTwo = b[j: j + 2]
        if(len(sequenceOne) == 2 and len(sequenceTwo) == 2):
            if(sequenceOne == sequenceTwo):
                counter += 1

    return counter 