# 최솟값 찾기
import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

# N : 데이터 개수, L : 슬라이딩 길이
N, L = map(int, input().split()) 
myqueue = deque()
ary = list(map(int, input().split()))

for i in range(N):
  while myqueue and myqueue[-1][0] > ary[i]:
    myqueue.pop()
  myqueue.append((ary[i], i))
  if myqueue[0][1] <= i - L: # 범위에서 벗어난 값은 덱에서 제거
    myqueue.popleft()
  print(myqueue[0][0], end = ' ')