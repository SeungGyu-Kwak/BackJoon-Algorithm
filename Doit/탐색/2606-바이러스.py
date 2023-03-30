# 바이러스
# bfs or dfs로 문제풀기

import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input()) # 컴퓨터 수 (노드)
M = int(input()) # 컴퓨터 쌍의 수 (에지)

A = [[] for _ in range(N+1)] # 인접리스트
visited = [False] * (N+1) # 방문리스트

# 인접그래프 생성
for i in range(M):
  s, e = map(int, input().split())
  A[s].append(e)
  A[e].append(s)

count = 0 # 바이러스에 걸린 바이러스 수

def dfs(v):
  global count
  visited[v] = True
  for i in A[v]:
    if not visited[i]:
      visited[i] = True
      count += 1
      dfs(i)

# 1번 컴퓨터 바이러스 감염 따라서 1번부터 dfs 탐색
dfs(1)
print(count)