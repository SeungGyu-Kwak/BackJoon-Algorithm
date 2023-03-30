# 최소 신장트리
# 유니온 파인드 구현해야 함
# 사이클 있어서는 안됨
import sys
from queue import PriorityQueue
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

V, E = map(int, input().split()) # 정점개수, 간선개수
pq = PriorityQueue()
parent = [0] * (V+1)
for i in range(1,V+1):
  parent[i] = i

for i in range(E):
  s, e, w = map(int, input().split())
  pq.put((w,s,e))

def find(a):
  if a == parent[a]:
    return a
  else:
    parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
  a = find(a)
  b = find(b)
  if a != b:
    parent[b] = a

useEdge = 0
result = 0

while useEdge < V-1:
  w, s, e = pq.get()
  if find(s) != find(e): # 같은 부모가 아닐때만 연결
    union(s,e)
    useEdge += 1
    result += w
print(result)

