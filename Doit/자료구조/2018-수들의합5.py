# 수들의 합 5

import sys
sys.stdin = open('input.txt', 'r')
input= sys.stdin.readline

N = int(input())
count, start, end = 1, 1, 1
sum = 1
while end != N:
  if sum < N:
    end += 1
    sum += end
  elif sum > N:
    sum -= start
    start += 1
  elif sum == N:
    count += 1
    end += 1
    sum += end

print(count)
