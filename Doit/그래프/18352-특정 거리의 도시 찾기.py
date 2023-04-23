# 특정 거리의 도시 찾기
import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, M, K, X = map(int, input().split())
A = [[] for _ in range(N+1)]
visited = [-1] * (N+1) # 방문리스트

for _ in range(M):
    s, e = map(int, input().split())
    A[s].append(e)


def BFS(v):
    queue = deque()
    visited[v] += 1 # 출발점은 거리가 0임 
    queue.append(v)
    
    while queue:
        nowNode = queue.popleft()
        for nextNode in A[nowNode]:
            if visited[nextNode] == -1:
              visited[nextNode] = (visited[nowNode] + 1)
              print(visited)
              queue.append(nextNode)

BFS(X)

answer = []
for i in range(N+1):
    if visited[i] == K:
        answer.append(i)

if not answer:
    print(-1)
else:
    answer.sort()
    for i in answer:
        print(i)
        
# print(visited)    
    
