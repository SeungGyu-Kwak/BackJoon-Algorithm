# 수 정렬하기

import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())

# 파이썬에서는 sort()로 쉽게할 수 있음
# 버블정렬로 풀어보자

ary = []
for i in range(N):
  ary.append(int(input()))

# 버블정렬
for i in range(N-1):
  for j in range(N-1-i):
    if ary[j] > ary[j+1]:
      tmp = ary[j]
      ary[j] = ary[j+1]
      ary[j+1] = tmp

for i in range(N):
  print(ary[i])