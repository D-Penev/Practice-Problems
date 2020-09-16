def birthday_cake_candles():
    n = int(input())
    candles = list(map(int, input().split()))
    maxCandleHeight = max(candles)
    totalMaxCandlesOfHeight = candles.count(maxCandleHeight)

    return totalMaxCandlesOfHeight

print(
    birthday_cake_candles()
)