# 촌수 계산
import sys
sys.setrecursionlimit(10**6)
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
num1, num2 = map(int, input().split())
m = int(input())

A = [[] for _ in range(N+1)] # 인접리스트
for _ in range(m):
  s, e = map(int, input().split())
  A[s].append(e)
  A[e].append(s)

count = 0 # 촌수저장값
visited = [False] * (N+1)
result = [0] * (N+1)

def dfs(v):
  visited[v] = True
  for i in A[v]:
    if not visited[i]:
      result[i] = result[v] + 1 #부모노드가 갖는 촌수에 +1 해줌
      dfs(i)

dfs(num1)
if result[num2] > 0:
  print(result[num2])
else:
  print(-1)

