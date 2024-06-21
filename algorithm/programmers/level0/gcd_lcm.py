# 최대공약수(gcd)
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

# 최소공배수(lcm)
def lcm(a, b):
    return int(a * b / gcd(a, b))

print(gcd(10, 5))
print(gcd(2, 4))
print(lcm(2, 3))
print(lcm(4, 24))