# 타임머신
# 벨만포드 알고리즘 사용
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split()) # 도시개수, 버스 노선의 개수
edges = [] # 엣지리스트
distance = [sys.maxsize] * (N+1)

for i in range(M): #에지 데이터 저장
  start, end, time = map(int, input().split())
  edges.append((start, end, time))

# 벨만포드 수행
distance[1] = 0

for _ in range(N-1):
  for start, end, time in edges:
    if distance[start] != sys.maxsize and distance[end] > distance[start] + time:
      distance[end] = distance[start] + time

# 음수사이클 확인
isCycle = False

for start, end, time in edges:
  if distance[start] != sys.maxsize and distance[end] > distance[start] + time:
    isCycle = True

if not isCycle:
  for i in range(2, N+1):
    if distance[i] != sys.maxsize:
      print(distance[i])
    else:
      print(-1)
else:
  print(-1)