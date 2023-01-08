# 트리의 지름

import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input()) # 정점의 개수(노드개수)
A = [[] for _ in range(N+1)] # 인접리스트
visited = [False] * (N+1) # 방문리스트
distance = [0] * (N+1) # 해당 노드에서 노드까지의 거리리스트

# 인접리스트 생성(노드번호, 가중치가 있으므로 튜플로 저장)
for i in range(N):
  numbers = list(map(int, input().split()))
  index = 0
  S = numbers[index]
  index += 1
  while True:
    E = numbers[index] # 노드번호
    if E == -1:
      break
    V = numbers[index + 1] # 가중치
    A[S].append((E, V))
    index += 2

def bfs(v):
  myqueue = deque()
  myqueue.append(v)
  visited[v] = True
  while myqueue:
    now = myqueue.popleft()
    for i in A[now]:
      if not visited[i[0]]:
        visited[i[0]] = True
        myqueue.append(i[0])
        distance[i[0]] = distance[now] + i[1]
bfs(1)
Max = 1
for i in range(2, N+1):
  if distance[Max] < distance[i]:
    Max = i
distance = [0] * (N+1)
visited = [False] * (N+1)
bfs(Max)
distance.sort()
print(distance[N])