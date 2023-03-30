# K 번째 최단경로 찾기
import sys
from queue import PriorityQueue
# 우선순위 큐를 사용하여 가중치가 낮은 것 부터 자동으로
# 오름차순 되도록 설정
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, M, K = map(int, input().split())
A = [[] for _ in range(N+1)] # 인접리스트

# 거리 리스트 
distance = [[sys.maxsize]*K for _ in range(N+1)]

for _ in range(M):
  s, e, w = map(int, input().split())
  A[s].append((e,w))

pq = PriorityQueue()

pq.put((0,1)) # 가중치 우선이기 때문에 가중치, 노드 순서로 저장
distance[1][0] = 0 # 시작도시 최단거리 저장

while pq.qsize() > 0:
  now = pq.get()
  cost = now[0]
  node = now[1]
  for nNode, nCost in A[node]:
    sCost = cost + nCost
    if distance[nNode][K-1] > sCost:
      distance[nNode][K-1] = sCost
      distance[nNode].sort()
      pq.put((sCost, nNode))

for i in range(1, N+1):
  if distance[i][K-1] == sys.maxsize:
    print(-1)
  else:
    print(distance[i][K-1])