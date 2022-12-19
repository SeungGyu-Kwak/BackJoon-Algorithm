# 수 정렬하기 3
# N이 10,000,000이라서 엄청 크므로 O(nlogn)으로는 못품
# 더 빠른 기수정렬 or 계수정렬로 풀어보자.
# 계수정렬로 풀자

import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
count = [0] * (N+1)

for i in range(1, N+1):
  count[int(input())] += 1

for i in range(1, N+1):
  if count[i] != 0:
    for _ in range(count[i]):
      print(i)
