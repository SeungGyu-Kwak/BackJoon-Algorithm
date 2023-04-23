# DFS와 BFS

import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, M, V = map(int, input().split()) # 정점개수, 간선개수, 탐색시작노드번호

# 변수 선언
A = [[] for _ in range(N+1)] # 인접리스트
myQueue = deque() # bfs를 위한 queue
visited = [False] * (N+1) # 노드방문 확인 리스트

# 인접리스트 생성
for _ in range(M):
  u, v = map(int ,input().split())
  A[u].append(v)
  A[v].append(u)

# dfs 메소드
def dfs(v):
  print(v, end = ' ')
  visited[v] = True
  for i in A[v]:
    if not visited[i]:
      dfs(i)
  
# bfs 메소드
def bfs(v):
  queue = deque()
  visited[v] = True
  queue.append(v)
  
  while queue:
    now = queue.popleft()
    print(now, end = " ")
    for i in A[now]:
      if not visited[i]:
        visited[i] = True
        queue.append(i)

dfs(V)
print()
visited = [False] * (N+1)
bfs(V)