# ABCDE

import sys
sys.setrecursionlimit(10 ** 6)
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split()) # 사람의 수, 친구관계 수
arrive = False
A = [[] for _ in range(N+1)]
visited = [False] * (N+1)

# 인접리스트 생성
for _ in range(M):
    s, e = map(int, input().split())
    A[s].append(e)
    A[e].append(s)

def dfs(v, depth):
    global arrive
    if depth == 4:
        arrive = True
        return
    
    visited[v] = True
    for i in A[v]:
        if not visited[i]:
            dfs(i, depth+1)
    visited[v] = False

dfs(0, 0)
if arrive:
    print(1)
else:
    print(0)