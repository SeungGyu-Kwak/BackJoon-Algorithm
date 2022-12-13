# 제로

import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

K = int(input())
stack = []
for k in range(K):
  num = int(input())
  if num == 0:
    stack.pop()
  else:
    stack.append(num)

print(sum(stack))