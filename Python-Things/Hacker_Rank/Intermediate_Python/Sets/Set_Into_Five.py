def intro_five():
    n = int(input())
    elements = set(map(int, input().split()))
    commandsNumber = int(input())

    for i in range(commandsNumber):
        curr = input().split()
        command = curr[0]

        if command == 'pop':
            if len(elements) != 0:
                elements.pop()
        elif command == 'remove':
             param = int(curr[1])
             if param in elements:
                 elements.remove(param)
        elif command == 'discard':
            elements.discard(int(curr[1]))

    return sum(elements)

print(
    intro_five()
)