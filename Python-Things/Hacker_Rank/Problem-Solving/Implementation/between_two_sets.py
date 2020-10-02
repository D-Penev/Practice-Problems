def between_two_sets():
    arr = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    gcd = _gcd_(a[0], a[1])
    lcm = _lcm_(a[0], a[1], gcd)
    lcm_increment = lcm
    print(32 % 12 == 0)
    is_factor = 0
    while True:
        test = len(list(filter(lambda x: x % lcm == 0, b)))
        if test == len(b):
            is_factor += 1
            lcm += lcm_increment
        

    return  is_factor

def _lcm_(a,b,gcd):
    return (a * b) / gcd

def _gcd_(a,b):
    if b == 0:
        return  a
    return  _gcd_(b, a % b)

print(
    between_two_sets()
)
