# 타임머신
# 벨만포드 알고리즘 사용

import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split()) # 도시의 개수, 버스 노선 개수
edges = [] # 엣지 리스트 생성
distance = [sys.maxsize] * (N+1) # 거리 리스트

# 에지 데이터 저장
for i in range(M):
  start, end, time = map(int, input().split())
  edges.append((start, end, time))

# 벨만포드 수행
distance[1] = 0 # 출발노드 0으로 초기화

for _ in range(N-1):
  for start, end, time in edges:
    if distance[start] != sys.maxsize and distance[end] > distance[start] + time:
      distance[end] = distance[start] + time

# 음수 사이클 확인
mCycle = False

for start, end, time in edges:
  if distance[start] != sys.maxsize and distance[end] > distance[start] + time:
    mCycle = True

if not mCycle:
  for i in range(2, N+1): # 1은 뺀다
    if distance[i] != sys.maxsize:
      print(distance[i])
    else: # 거리가 INF일 때는 -1을 출력
      print(-1)
else:
  print(-1)