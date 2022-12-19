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

# 인접리스트 초기화
for i in range(M):
  s, e = map(int, input().split())
  A[s].append(e)
  A[e].append(s)
for i in range(1, N+1): # 노드번호가 작은 것을 먼저 방문하기위해 오름차순으로 정렬
  A[i].sort()


# dfs 함수
def dfs(v):
  visited[v] = True
  print(v, end = ' ')
  for i in A[v]:
    if not visited[i]:
      dfs(i)

# bfs 함수
def bfs(v):
  myQueue.append(v)
  visited[v] = True
  while myQueue:
    now_Node = myQueue.popleft()
    print(now_Node, end = ' ')
    for i in A[now_Node]:
      if not visited[i]:
        visited[i] = True
        myQueue.append(i)

dfs(V)
visited = [False] * (N+1) # 리스트 초기화
print()
bfs(V)



