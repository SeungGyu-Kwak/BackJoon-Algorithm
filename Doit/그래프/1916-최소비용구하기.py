# 최소비용 구하기
# 다익스트라
import sys
from queue import PriorityQueue
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input()) # 도시 개수
M = int(input()) # 버스 개수
A = [[] for _ in range(N+1)] # 인접리스트
dist = [sys.maxsize] * (N+1)
visited = [False] * (N+1)

for _ in range(M):
  s, e, w = map(int, input().split())
  A[s].append((e,w))

start, end = map(int, input().split())

def dijkstra(start, end):
  pq = PriorityQueue()
  pq.put((0, start))
  dist[start] = 0
  while pq.qsize() > 0:
    nowNode = pq.get()
    now = nowNode[1]
    if not visited[now]:
      visited[now] = True
      for n in A[now]:
        if not visited[n[0]] and dist[n[0]] > dist[now] + n[1]:
          dist[n[0]] = dist[now] + n[1]
          pq.put((dist[n[0]], n[0]))
  return dist[end]

print(dijkstra(start, end))
