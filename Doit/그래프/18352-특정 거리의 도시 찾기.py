# 특정 거리의 도시 찾기
import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, M, K, X = map(int, input().split())
A = [[] for _ in range(N+1)] # 인접리스트 생성
# 인접리스트 받기
for _ in range(M):
  a, b = map(int ,input().split())
  A[a].append(b) # 단방향이라서 한 번만 값 삽입

answer = [] # 최단 거리가 K인 도시 번호 저장할 리스트
visited = [-1] * (N+1) # 방문리스트

def bfs(v):
  myQueue = deque() # 큐 생성
  myQueue.append(v) # 노드 큐에 삽입
  visited[v] += 1 # 첫번째 시작 노드는 0으로 해줌
  while myQueue: # 큐가 빌떄까지
    nowNode = myQueue.popleft()
    for i in A[nowNode]:
      if visited[i] == -1: # 아직 방문 안했으면
        visited[i] = visited[nowNode] + 1
        myQueue.append(i)

bfs(X)

for i in range(N+1):
  if visited[i] == K:
    answer.append(i)
answer.sort()

if not answer:
  print(-1)
else:
  for i in answer:
    print(i)