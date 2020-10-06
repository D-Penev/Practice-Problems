def between_two_sets():
    arr = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    gcd = _gcd_(a[0], a[1])
    lcm = _lcm_(a[0], a[1], gcd)
    lcm_increment = lcm
    is_factor = 0
    while True:
        for i in range(len(a)):
            if lcm % a[i] == 0:
                is_factor += 1
        for i in range(len(b)):
            if b[i] % lcm == 0:
                is_factor += 1

        lcm += lcm_increment

    return  is_factor

def _lcm_(a,b,gcd):
    return (a * b) / gcd

def _gcd_(a,b):
    if b == 0:
        return  a
    return  _gcd_(b, a % b)

def _calculate_gcf(arr):
    _common_factors = []
    for i in range(len(arr)):
        for j in range(0, arr[i]):
            if arr[i] % j == 0:
                _common_factors.append(j)

    return max(_common_factors)

print(
    between_two_sets()
)
