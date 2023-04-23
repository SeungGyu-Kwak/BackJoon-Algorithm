# 미로탐색
# 완전탐색 문제 ,bfs로 푼다.
import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split()) # N x M 크기의 배열을 위한 값 받기
A = [] # 그래프 받기 위한 리스트 생성
for i in range(N):
    tmpList = list(map(int, input().strip()))
    A.append(tmpList)

visited = [[False] * M for _ in range(N)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def BFS(i, j):
    visited[i][j] = True
    queue = deque()
    queue.append((i,j))
    while queue:
        now_node = queue.popleft()
        for k in range(4):
            nx = now_node[0] + dx[k]
            ny = now_node[1] + dy[k]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if A[nx][ny] != 0 and not visited[nx][ny]:
                visited[nx][ny] = True
                A[nx][ny] = A[now_node[0]][now_node[1]] + 1
                queue.append((nx, ny))

BFS(0,0)
print(A[N-1][M-1])
            
            
    
    
    