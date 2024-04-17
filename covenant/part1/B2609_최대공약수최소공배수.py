import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

# 유클리드호제법 (최대공약수 구하기)
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

num1, num2 = map(int, input().split())
# 최소공배수 구하기 -> 두 수의 곱 / 최대공약수
lcm = int(num1 * num2 / gcd(num1,num2))
print(gcd(num1, num2))
print(lcm)