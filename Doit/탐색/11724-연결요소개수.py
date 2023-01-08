# 연결 요소의 개수
# dfs로 문제 해결해보기
import sys
sys.setrecursionlimit(10 ** 6)
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split()) # 노드의 개수, 에지의 개수
A = [[] for _ in range(N+1)] # 인접리스트
visited = [False] * (N+1) # 방문리스트

# 인접리스트 만들기
for _ in range(M):
  u, v = map(int, input().split())
  A[u].append(v)
  A[v].append(u)

# dfs
def dfs(v):
  visited[v] = True
  for i in A[v]:
    if not visited[i]:
      dfs(i)

count = 0
for i in range(1, N+1):
  if not visited[i]: # 연결 노드 중 방문하지 않았던 노드만 탐색
    count += 1
    dfs(i)
print(count)


