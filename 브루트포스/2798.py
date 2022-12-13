# 블랙잭 

import sys
sys.stdin = open('input.txt', 'r')
N, M = map(int, input().split())
card = list(map(int, sys.stdin.readline().split()))

tmp = []
result = 0
for i in range(N):
  for j in range(i+1, N):
    for k in range(j+1, N):
      if card[i] + card[j] + card[k] > M:
        continue
      else:
        result = max(result, card[i] + card[j] + card[k])

print(result)

