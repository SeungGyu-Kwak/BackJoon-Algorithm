# K 번째 최단경로 찾기
import sys
from queue import PriorityQueue

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, M, K = map(int, input().split()) 
W = [[] for _ in range(N+1)] # 인접리스트
distance = [[sys.maxsize]* K for _ in range(N+1)] # 거리리스트

# 인접리스트 초기화
for i in range(M):
  a, b, c = map(int, input().split())
  W[a].append((b,c))

pq = PriorityQueue() # 우선순위 큐 생성
pq.put((0,1)) # 가중치 우선이라서 가중치, 목표노드 순으로 저장
distance[1][0] = 0

while pq.qsize() > 0 :
  current = pq.get()
  c_v = current[1] # 노드
  c_c = current[0] # 가중치
  for nNode, nCost in W[c_v]:
    sCost = c_c + nCost
    if distance[nNode][K-1] > sCost:
      distance[nNode][K-1] = sCost
      distance[nNode].sort()
      pq.put((sCost, nNode))


for i in range(1, N+1):
  if distance[i][K-1] == sys.maxsize:
    print(-1)
  else:
    print(distance[i][K-1])