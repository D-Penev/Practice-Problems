def Symmetrical_Difference():
    n = int(input())
    setA = set(map(int, input().split()))
    m  = int(input())
    setB = set(map(int, input().split()))
    results = list(list(setA.difference(setB)) + list(setB.difference(setA)))
    results.sort()
    for i in results:
        print(i)
        
Symmetrical_Difference()