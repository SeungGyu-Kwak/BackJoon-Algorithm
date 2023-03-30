import sys
import copy
from collections import deque
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

dx = [0,0,1,-1]
dy = [1,-1,0,0]

# bfs로 탐색하기
def BFS():
  queue = deque()
  tmp_graph = copy.deepcopy(graph)

  for i in range(N):
    for j in range(M):
      if tmp_graph[i][j] == 2:
        queue.append((i,j))
  
  while queue:
    r, c = queue.popleft()

    for i in range(4):
      nx = r + dx[i]
      ny = c + dy[i]

      if nx >= 0 and nx < N and ny >=0 and ny < M:
        if tmp_graph[nx][ny] == 0:
          tmp_graph[nx][ny] = 2
          queue.append((nx, ny))

  global result
  count = 0
  for i in range(N):
    for j in range(M):
      if tmp_graph[i][j] == 0:
        count += 1
  
  result = max(result, count)

# dfs로 벽을 3개 만든다.
def DFS(n):
  if n == 3:
    BFS()
    return
  for i in range(N):
    for j in range(M):
      if graph[i][j] == 0:
        graph[i][j] = 1
        DFS(n+1)
        graph[i][j] = 0


###################
N, M = map(int, input().split())
graph = []


for i in range(N):
  tmpAry = list(map(int, input().split()))
  graph.append(tmpAry)

result = 0
# 벽 세우기
DFS(0)
print(result)





