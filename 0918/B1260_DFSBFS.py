import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N, M, V = map(int, input().split())
ary = [[] for _ in range(N+1)]

for i in range(M):
  s, e = map(int, input().split())
  ary[s].append(e)
  ary[e].append(s)

for i in range(1,N+1):
  ary[i].sort()

# 방문리스트
visited = [False] * (N+1)

def dfs(v):
  visited[v] = True
  print(v, end = " ")
  for i in ary[v]:
    if not visited[i]:
      dfs(i)

def bfs(v):
  queue = deque()
  queue.append(v)
  visited[v] = True
  while queue:
    now = queue.popleft()
    print(now, end = " ")
    for i in ary[now]:
      if not visited[i]:
        visited[i] = True
        queue.append(i)

dfs(V)
print()
visited = [False] * (N+1)
bfs(V)