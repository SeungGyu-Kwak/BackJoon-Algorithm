# 효율적인 해킹
# 그래프 완전 탐색이므로 bfs를 통해 풀이 진행해보자
import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split()) # 컴퓨터개수, 신뢰관계
A = [[] for _ in range(N+1)] # 인접리스트 만듦
answer = [0] * (N+1) # 정답리스트(신뢰를 받는 횟수 저장)

def bfs(v):
  myQueue = deque()
  myQueue.append(v)
  visited[v] = True
  while myQueue:
    nowNode = myQueue.popleft()
    for i in A[nowNode]:
      if not visited[i]:
        visited[i] = True
        answer[i] += 1 # 신뢰받는 횟수 +1 해줌
        myQueue.append(i)

for _ in range(M):
  s, e = map(int, input().split())
  A[s].append(e)


# 모든 노드에서 차례로 bfs 수행해본다.
for i in range(1, N+1):
  visited = [False] * (N+1)
  bfs(i)

# answer에 저장된 값들 중 가장 큰 값을 가지고 옴
maxValue = 0
for i in range(1, N+1):
  maxValue = max(maxValue, answer[i])

for i in range(1, N+1):
  if answer[i] == maxValue:
    print(i, end =' ')

