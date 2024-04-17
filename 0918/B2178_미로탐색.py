import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N, M = map(int, input().split())
ary = []
for i in range(N):
  tmp = list(map(int, input().strip()))
  ary.append(tmp)
# print(ary)

dx, dy = [-1, 1, 0, 0], [0,0,-1,1]
visited = [[False] * M for _ in range(N)]

def bfs(i, j):
  queue = deque()
  queue.append((i,j))
  visited[i][j] = True
  
  while queue:
    nowX, nowY = queue.popleft()
    for i in range(4):
      nx, ny = nowX + dx[i], nowY + dy[i]
      if 0 <= nx < N and 0 <= ny < M and ary[nx][ny] != 0:
        if not visited[nx][ny]:
          ary[nx][ny] += ary[nowX][nowY]
          queue.append((nx,ny))
          visited[nx][ny] = True

bfs(0,0)
print(ary[N-1][M-1])