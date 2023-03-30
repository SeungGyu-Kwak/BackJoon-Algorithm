# 정수를 1로 만들기

import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input()) # 정수 N 받기
D = [0] * (N+1) # DP테이블
D[1] = 0 # 1일 때는 연산 불필요

for i in range(2, N+1):
  D[i] = D[i-1] + 1 # 1빼기 연산
  if i % 2 == 0: # 나누기 2 연산
    D[i] = min(D[i], D[i // 2] + 1) 
  if i % 3 == 0: # 나누기 3 연산
    D[i] = min(D[i], D[i // 3] + 1)

print(D[N])
