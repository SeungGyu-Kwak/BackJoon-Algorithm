# 분해합

import sys
sys.stdin = open('input.txt', 'r')
N = int(input())

isTrue = False
for i in range(1,N):
  ary = []
  sum = 0
  for t in str(i):
    ary.append(t)
  sum += i
  for j in ary:
    sum += int(j)
  if sum == N:
    isTrue = True
    break

if isTrue:
  print(i)
else:
  print(0)
