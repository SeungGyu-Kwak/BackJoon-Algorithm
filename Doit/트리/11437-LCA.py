import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
from collections import deque

N = int(input()) # 노드의 개수
tree = [[] for _ in range(N+1)] # 트리데이터 저장

# 인접리스트 생성
for _ in range(0, N-1):
    s, e = map(int, input().split())
    tree[s].append(e)
    tree[e].append(s)
depth = [0] * (N+1) # 노드 깊이 리스트
parent = [0] * (N+1) # 부모 저장 리스트
visited = [False] * (N+1)

def BFS(node):
    queue = deque()
    queue.append(node)
    visited[node] = True
    level = 1
    now_size = 1
    count = 0

    while queue:
      now_node = queue.popleft()
      for next in tree[now_node]:
        if not visited[next]:
          visited[next] = True
          queue.append(next)
          parent[next] = now_node # 부모노드 저장
          depth[next] = level # 노드 깊이 저장
      count += 1
      if count == now_size: # 현재 깊이의 모든 노드를 방문
         count = 0
         now_size = len(queue)
         level += 1
BFS(1)

def executeLCA(a, b):
  if depth[a] < depth[b]:
      temp = a
      a = b
      b = temp
  
  while depth[a] != depth[b]:
    a = parent[a]
  
  while a != b:
     a = parent[a]
     b = parent[b]

  return a
M = int(input())

for _ in range(M):
  a, b= map(int, input().split())
  print(str(executeLCA(a,b)))
