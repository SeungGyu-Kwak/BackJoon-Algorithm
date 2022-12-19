# 미로탐색
# 완전탐색 문제 , bfs로 푼다.

import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
N, M = map(int, input().split())
A = [[0]* M for _ in range(N)]
visited = [[False]*M for _ in range(N)]

# 미로 입력받기
for i in range(N):
  numbers = list(input().strip())
  for j in range(M):
    A[i][j] = int(numbers[j])

def bfs(i, j):
  queue = deque()
  queue.append((i,j))
  visited[i][j] = True

  while queue:
    now = queue.popleft()
    for k in range(4): # 상하좌우검색
      x = now[0] + dx[k]
      y = now[1] + dy[k]
      if x >= 0 and y >= 0 and x < N and y < M: #유효한 좌표
        if A[x][y] != 0 and not visited[x][y]: # 이동할 수 있는 칸이면서 방문하지 않은 노드
          visited[x][y] = True # 방문기록
          A[x][y] = A[now[0]][now[1]] + 1 # A리스트에 depth를 현재 노드의 depth + 1로 업데이트
          queue.append((x,y)) # 큐에 데이터 삽입

bfs(0,0)
print(A[N-1][M-1])