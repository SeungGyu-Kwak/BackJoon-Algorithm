# 최솟값 찾기
import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, L = map(int, input().split())
A = list(map(int, input().split()))
myqueue = deque()

for i in range(N):
  while myqueue and myqueue[-1][0] > A[i]:
    myqueue.pop()
  myqueue.append((A[i], i))
  if myqueue[0][1] <= i - L:
    myqueue.popleft()
  print(myqueue[0][0], end=' ')