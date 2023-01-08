# 트리 부모 찾기
import sys
sys.setrecursionlimit(1000000)
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input()) # 노드 개수
visited = [False] * (N+1) # 방문여부 체크 리스트
tree = [[] for _ in range(N+1)] # 트리 (인접리스트)
answer = [0] * (N+1)
for _ in range(1, N): # 인접리스트 저장
  n1, n2 = map(int, input().split())
  tree[n1].append(n2)
  tree[n2].append(n1)

# DFS 함수
def dfs(number):
  visited[number] = True
  for i in tree[number]:
    if not visited[i]:
      answer[i] = number
      dfs(i)

dfs(1)
for i in range(2, N+1):
  print(answer[i])

