# 연결 요소의 개수
# dfs로 문제 해결해보기
import sys
sys.setrecursionlimit(10 ** 6)
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split())

A = [[] for _ in range(N+1)]
visited = [False] * (N+1)

# 인접리스트 만들기
for i in range(M):
    s, e = map(int, input().split())
    A[s].append(e)
    A[e].append(s)

count = 0

def dfs(v):
    visited[v] = True
    for i in A[v]:
        if not visited[i]:
            dfs(i)

for i in range(1, N+1):
    if not visited[i]:
        count += 1
        dfs(i)
print(count)
