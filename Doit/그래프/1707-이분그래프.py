# 이분그래프
import sys
sys.stdin = open('input.txt', 'r')
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

K = int(input()) # 테스트 케이스
isEven = True

def dfs(v):
  global isEven
  visited[v] = True
  for i in A[v]:
    if not visited[i]:
      # 인접노드는 같은 집합 x
      check[i] = (check[v] + 1) % 2
      dfs(i)
    # 이미 방문한 노드가 현재 내 노드와 같은 집합이면 이분그래프 아님
    elif check[v] == check[i]:
      isEven = False

for _ in range(K):
  V, E = map(int, input().split()) # 정점개수, 간선개수
  A = [[] for _ in range(V+1)] # 인접리스트
  visited = [False] * (V+1) # 방문체크리스트
  check = [0] * (V+1) # 집합 구분 리스트
  isEven = True
  for i in range(E): # 인접리스트 값 저장
    s, e = map(int, input().split())
    A[s].append(e)
    A[e].append(s)

  for i in range(1, V+1):
    if isEven:
      dfs(i)
    else:
      break
  
  if isEven:
    print('YES')
  else:
    print('NO')