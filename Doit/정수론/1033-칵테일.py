# 칵테일
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input()) # 종류 개수
A = [[] for _ in range(N)] # 인접리스트
visited = [False] * N # 방문체크여부
lcm = 1 # 최소공배수 
D = [0] * N

# 최대공약수 구하는 함수
def gcd(a, b):
  if b == 0:
    return a
  else:
    return gcd(b, a % b)

def dfs(v):
  visited[v] = True
  for i in A[v]:
    next = i[0]
    if not visited[next]:
      D[next] = D[v] * i[2] // i[1]
      dfs(next)

for i in range(N-1):
  a, b, p, q = map(int, input().split())
  A[a].append((b, p, q))
  A[b].append((a, q, p))
  lcm *= (p*q // gcd(p,q)) # 최소공배수 = a * b / ab의 최대공약수

D[0] = lcm # 시작점에 최소공배수 입력
dfs(0)
mgcd = D[0]
for i in range(1, N):
  mgcd = gcd(mgcd, D[i])

for i in range(N):
  print(int(D[i] // mgcd), end = ' ')