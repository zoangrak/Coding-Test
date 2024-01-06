'''유클리드 호제법'''
a, b = map(int, input().split())

# a = bq + r
# gcd(a, b) == gcd(b, r)
def gcd(a, b):
  while b > 0:
    a, b = b, a % b
  return a

# a, b의 최소공배수는 a와 b의 곱을 gcd(a, b)로 나눈 것과 같다
def lcm(a, b):
  return a * b // gcd(a, b)
  
print(gcd(a, b))
print(lcm(a, b))

# import math

# a, b = map(int, input().split())

# print(math.gcd(a, b))
# print(math.lcm(a, b))

