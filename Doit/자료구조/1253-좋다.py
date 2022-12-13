# 좋다

import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
ary = list(map(int, input().split()))

ary.sort()
count = 0
for n in range(N):
  i = 0
  j = N - 1
  target = ary[n]
  while i < j:
    if i == n:
      i += 1
      continue
    if j == n:
      j -= 1
      continue
    if ary[i] + ary[j] == target:
      count += 1
      break
    elif ary[i] + ary[j] < target:
      i += 1
    elif ary[i] + ary[j] > target:
      j -= 1
print(count)

