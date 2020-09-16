def list_basics():
    n = int(input())
    storageList = []
    for i in range(0, n):
        cmdArgs = input().split()
        command = cmdArgs[0]
        if command == 'append':
            storageList.append(int(cmdArgs[1]))
        elif command == 'print':
            print(storageList)
        elif command == 'remove':
            storageList.remove(int(cmdArgs[1]))
        elif command == 'insert':
            index = int(cmdArgs[1])
            valueToInsert = int(cmdArgs[2])
            storageList.insert(index, valueToInsert)
        elif command == 'sort':
            storageList.sort()
        elif command == 'pop':
            storageList.pop()
        elif command == 'reverse':
            storageList.reverse()

list_basics()
