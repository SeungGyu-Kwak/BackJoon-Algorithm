# 오민식의 고민
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, sCity, eCity, M = map(int, input().split())
edges = [] # 엣지리스트
distance = [-sys.maxsize] * (N)

for _ in range(M):
  s, e, m = map(int, input().split())
  edges.append((s,e,m))

# 각 도시 벌 수 있는 돈 저장
cityMoney = list(map(int, input().split()))

distance[sCity] = cityMoney[sCity]

for i in range(N+101):
  for start, end, price in edges:
    if distance[start] == -sys.maxsize:
      continue
    elif distance[start] == sys.maxsize:
      distance[end] = sys.maxsize
    elif distance[end] < distance[start] + cityMoney[end] - price:
      distance[end] = distance[start] + cityMoney[end] - price
      if i >= N-1:
        distance[end] = sys.maxsize

if distance[eCity] == -sys.maxsize:
  print('gg')
elif distance[eCity] == sys.maxsize:
  print('Gee')
else:
  print(distance[eCity])