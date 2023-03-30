# 트리
import sys
sys.setrecursionlimit(1000000)
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input()) # 노드 개수
A = [[] for _ in range(N)] # 인접리스트
visited = [False] * (N)
answer = 0
p = list(map(int, input().split()))

for i in range(N):
  if p[i] != -1:
    A[i].append(p[i])
    A[p[i]].append(i)
  else:
    root = i

deleteNode = int(input())

def dfs(number):
  global answer
  visited[number] = True
  cNode = 0
  for i in A[number]:
    if not visited[i] and i != deleteNode:
      cNode += 1
      dfs(i)
  if cNode == 0: # 자식 노드 수가 0일 때 정답에 추가
    answer += 1

if deleteNode == root: # 루트노드가 삭제되면 모두삭제
  print(0)
else:
  dfs(root)
  print(answer)