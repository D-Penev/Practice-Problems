def calculate_average():
    n = int(input())
    plants = set(map(int, input().split()))
    return sum(plants) / len(plants)