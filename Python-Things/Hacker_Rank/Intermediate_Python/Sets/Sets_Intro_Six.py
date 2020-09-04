def intro_six():
     english = int(input())
     enlighsNums = set(map(int, input().split()))
     french = int(input())
     frenchNums = set(map(int,input().split()))

     return len(enlighsNums.union(frenchNums))


print(
    intro_six()
)