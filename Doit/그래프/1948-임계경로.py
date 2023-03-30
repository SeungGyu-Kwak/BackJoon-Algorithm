# 임계경로 
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
from collections import deque

N = int(input()) # 도시의 개수
M = int(input()) # 도로의 개수
A = [[] for _ in range(N+1)] # 인접리스트
indegree= [0] * (N+1)
reverseA= [[] for _ in range(N+1)] # 역방향 인접리스트

for i in range(M):
  s, e, v = map(int, input().split())
  A[s].append((e,v))
  reverseA[e].append((s,v)) # 역방향 에지정보 저장
  indegree[e] += 1 # 진입차수 저장

startDosi, endDosi = map(int, input().split())

queue = deque()
queue.append(startDosi)
result = [0] * (N+1)

while queue: # 위상정렬 수행
  now = queue.popleft()
  for next in A[now]:
    indegree[next[0]] -= 1
    result[next[0]] = max(result[next[0]], result[now] + next[1])
    if indegree[next[0]] == 0:
      queue.append(next[0])

resultCount = 0 
visited = [False] * (N+1) 
queue.clear()
queue.append(endDosi)
visited[endDosi] = True

while queue: # 역방향 위상정렬 수행
  now = queue.popleft()
  for next in reverseA[now]:
    # 1분도 쉬지않는 도로 체크
    if result[next[0]] + next[1] == result[now]:
      resultCount += 1
      if not visited[next[0]]:
        visited[next[0]] = True
        queue.append(next[0])

print(result[endDosi])
print(resultCount)