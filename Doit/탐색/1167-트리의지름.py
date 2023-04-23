# 트리의 지름

import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input()) # 정점의 개수(노드개수)
A = [[] for _ in range(N+1)] # 인접리스트
visited = [False] * (N+1) # 방문리스트
distance = [0] * (N+1) # 해당 노드에서 노드까지의 거리리스트

# 인접리스트 생성(노드번호, 가중치가 있으므로 튜플로 저장)
for i in range(N):
    data = list(map(int, input().split()))
    S = data[0]
    index = 1
    while True:
        if data[index] == -1:
            break
        E = data[index]
        V = data[index + 1]
        A[S].append((E,V))
        index += 2

# 임의 노드에서 BFS로 탐색해 가장 거리가 먼 노드를 선택하자
# 우선 BFS 함수 만들기
def BFS(v):
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue:
        now_node = queue.popleft()
        for n in A[now_node]:
            if not visited[n[0]]:
                visited[n[0]] = True
                queue.append(n[0])
                distance[n[0]] = distance[now_node] + n[1] 
BFS(1)
Max = 1
for i in range(2, N+1):
    if distance[Max] < distance[i]:
        Max = i
        
distance = [0] * (N+1)
visited = [False] * (N+1)
BFS(Max)
distance.sort()
print(distance[N])
            