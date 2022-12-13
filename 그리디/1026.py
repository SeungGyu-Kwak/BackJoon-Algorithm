# 보물

import sys
# sys.stdin = open('input.txt', 'r')

N = int(input())
aryA = list(map(int, sys.stdin.readline().split()))
aryB = list(map(int, sys.stdin.readline().split()))

result = 0

for i in range(N):
  result += min(aryA) * max(aryB)
  aryA.pop(aryA.index(min(aryA)))
  aryB.pop(aryB.index(max(aryB)))
print(result)