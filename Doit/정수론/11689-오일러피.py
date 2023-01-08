# GCD(n,k) = 1

import sys
import math
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
result = N

for p in range(2, int(math.sqrt(N)) + 1): # 제곱근까지만 진행
  if N % p == 0: # p가 소인수 인지 확인
    result -= result / p
    while N % p == 0:
      N /= p

if N > 1: # 반복문에서 제곱근까지만 탐색했으므로 1개의 소인수가 누락되는 케이스 처리
  result -= result / N

print(int(result))