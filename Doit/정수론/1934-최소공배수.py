# 최소공배수
# a, b의 최소공배수 -> a * b / a와b의 최대공약수

import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

T = int(input()) # 테스트케이스

# 유클리드 호제법으로 최대공약수 구하기
def gcd(a, b):
  if b == 0:
    return a
  else:
    return gcd(b, a % b)

for t in range(T):
  a, b = map(int, input().split())
  result = a * b / gcd(a, b) # 최소공배수
  print(int(result))