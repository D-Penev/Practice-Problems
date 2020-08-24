def array123(arr):
    flag = False
    for i in range(len(arr)):
       currentSequence = ''.join([str(elem) for elem in arr[i: i+3]])
       if(currentSequence == '123'):
           flag = True
    
    return flag