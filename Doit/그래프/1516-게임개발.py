# 게임 개발

import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
from collections import deque

N = int(input()) # 건물 수
A = [[] for _ in range(N+1)] # 인접리스트
indegree = [0] * (N+1) # 인접차수리스트
selfbuild = [0] * (N+1) # 자기 자신을 짓는데 걸리는 시간

for i in range(1, N+1):
  inputlist = list(map(int, input().split()))
  selfbuild[i] = inputlist[0]
  index = 1
  while True:
    preTemp = inputlist[index]
    index += 1
    if preTemp == -1:
      break
    A[preTemp].append(i)
    indegree[i] += 1
  
queue = deque()

for i in range(1, N+1):
  if indegree[i] == 0:
    queue.append(i)

result = [0] * (N+1)

while queue:
  now = queue.popleft()
  for next in A[now]:
    indegree[next] -= 1
    result[next] = max(result[next], result[now] + selfbuild[now])
    if indegree[next] == 0:
      queue.append(next)

for i in range(1, N+1):
  print(result[i] + selfbuild[i])