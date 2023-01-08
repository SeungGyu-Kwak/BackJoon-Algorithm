# 최소 신장트리
# 유니온 파인드 구현해야 함
# 사이클 있어서는 안됨
import sys
from queue import PriorityQueue
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

V, E = map(int, input().split()) # 정점개수, 간선개수
pq = PriorityQueue() # 에지 정보를 저장할 우선순위 큐
parent = [0] * (V+1) # 대표 노드 저장 리스트
for i in range(V+1):
  parent[i] = i

for i in range(E):
  s, e, w = map(int ,input().split())
  pq.put((w, s, e)) # 가중치 기준이므로 w 먼저 넣기

# find 메소드 구현
def find(a):
  if a == parent[a]: # a의 대표 노드가 a라면
    return a
  else:
    parent[a] = find(parent[a])
    return parent[a]

# union 메소드 구현
def union(a, b):
  a = find(a)
  b = find(b)
  if a != b:
    parent[b] = a

# MST 실행
useEgde = 0 # 사용 에지 수 저장 변수
result = 0 # 정답

while useEgde < V-1:
  w, s, e = pq.get()
  if find(s) != find(e): #같은 부모가 아닌 경우만 연결
    union(s, e)
    result += w
    useEgde += 1

print(result)