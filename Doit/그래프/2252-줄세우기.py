# 줄 세우기
import sys
sys.stdin = open('input.txt', 'r')
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split()) # 학생 수, 비교횟수
A = [[] for _ in range(N+1)] # 인접리스트
indegree = [0] * (N+1) # 진입차수리스트

for i in range(M):
  S, E = map(int, input().split())
  A[S].append(E)
  indegree[E] += 1

queue = deque()

# indegree 리스트 값이 0인 노드를 큐에 삽입
for i in range(1, N+1):
  if indegree[i] == 0:
    queue.append(i)

while queue:
  now = queue.popleft()
  print(now, end = ' ')
  for next in A[now]:
    indegree[next] -= 1
    if indegree[next] == 0:
      queue.append(next)