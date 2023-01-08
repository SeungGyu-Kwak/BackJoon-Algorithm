# 수 정렬하기

import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())

# 파이썬에서는 sort()로 쉽게할 수 있음
# 버블정렬로 풀어보자

# 값 받기
A = []
for i in range(N):
  A.append(int(input()))

# 버블소트
for i in range(N-1):
  for j in range(N-1-i):
    if A[j] > A[j+1]:
      tmp = A[j+1]
      A[j+1] = A[j]
      A[j] = tmp

for i in range(N):
  print(A[i])