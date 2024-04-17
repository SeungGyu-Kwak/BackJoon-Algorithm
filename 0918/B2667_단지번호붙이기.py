import sys
sys.setrecursionlimit(10 ** 6)
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
ary = []
for i in range(N):
  tmp = list(map(int, input().strip()))
  ary.append(tmp)

visited = [[False] * N for _ in range(N)]

def dfs(i,j):
  global home
  dx, dy = [-1,1,0,0], [0,0,-1,1]
  
  if 0 <= i < N and 0 <= j < N and not visited[i][j]:
    if ary[i][j] == 1:
      visited[i][j] = True
      home += 1
      for k in range(4):
        dfs(i + dx[k], j + dy[k])
      return True   
  
  return False

dangi = 0 # 총 단지 수 받을 변수
count = [] # 단지 내 집의 수를 세는 리스트
home = 0
for i in range(N):
  for j in range(N):
    if dfs(i,j) == True:
      dangi += 1
      count.append(home)
      home = 0
print(dangi)
count.sort()
for c in count:
  print(c)