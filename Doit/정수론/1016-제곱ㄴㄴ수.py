# 제곱 ㄴㄴ 수
# 일반적인 반복문으로 풀면 시간 초과 남
# 에라토스테네스의 체 방식으로 접근하여 시간 최소화해야 함

import sys
import math
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

Min, Max = map(int, input().split())
Check = [False] * (Max - Min + 1)

for i in range(2, int(math.sqrt(Max) + 1)):
  pow = i * i
  start_index = int(Min / pow)
  if Min % pow != 0:
    start_index += 1
  for j in range(start_index, int(Max/pow) + 1):
    Check[int((j*pow) - Min)] = True

count = 0

for i in range(0, Max - Min + 1):
  if not Check[i]:
    count += 1

print(count)