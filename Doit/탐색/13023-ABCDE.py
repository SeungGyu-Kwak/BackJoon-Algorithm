# ABCDE

import sys
sys.setrecursionlimit(10 ** 6)
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split()) # 사람의 수, 친구관계 수
arrive = False
A = [[] for _ in range(N+1)]
visited = [False] * (N+1)

def dfs(now, depth):
  global arrive
  if depth == 5:
    arrive = True
    return
  visited[now] = True
  for i in A[now]:
    if not visited[i]:
      dfs(i, depth+1) # 재귀호출마다 깊이 증가
  visited[now] = False

for _ in range(M):
  s, e = map(int, input().split())
  A[s].append(e)
  A[e].append(s)

for i in range(N):
  dfs(i,1)
  if arrive:
    break

if arrive:
  print(1)
else:
  print(0)
