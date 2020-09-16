def very_big_sum():
    n = int(input())
    return sum(list(map(int, input().split())))

print(
    very_big_sum()
)