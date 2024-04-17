import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
M = int(input())

ary = [[] for _ in range(N+1)]
for _ in range(M):
  s, e = map(int, input().split())
  ary[s].append(e)
  ary[e].append(s)

answer = -1
visited = [False] * (N+1)
def dfs(v):
  global answer
  answer += 1
  #print(v, end=" ")
  visited[v] = True
  for i in ary[v]:
    if not visited[i]:
      dfs(i)

dfs(1)
print(answer)

  
