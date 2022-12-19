# 신기한 소수
# dfs로 탐색해서 살펴보기
# 일의자리 소수 : 2, 3, 5, 7

import sys
import math
sys.setrecursionlimit(10 ** 6)
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input()) # 자리수

# 소수 판별함수
def isPrime(n):
  for i in range(2, int(math.sqrt(n) + 1)):
    if n % i == 0:
      return False
  return True

def dfs(number):
  if len(str(number)) == N:
    print(number)
  else:
    for i in range(1, 10):
      if i % 2 == 0:
        continue
      if isPrime(number * 10 + i):
        dfs(number * 10 + i)
dfs(2)
dfs(3)
dfs(5)
dfs(7)
