# 트리 부모 찾기
import sys
sys.setrecursionlimit(1000000)
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input()) # 노드 개수
A = [[] for _ in range(N+1)]
visited = [False] * (N+1)
answer = [0] * (N+1)

for _ in range(1, N):
  s, e = map(int, input().split())
  A[s].append(e)
  A[e].append(s)

def dfs(number):
  visited[number] = True
  for i in A[number]:
    if not visited[i]:
      answer[i] = number
      dfs(i)
dfs(1)
for i in range(2, N+1):
  print(answer[i])
