# 거짓말
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, M = map(int,input().split())
trueP = list(map(int, input().split()))
T = trueP[0]
del trueP[0]

result = 0
party = [[] for _ in range(M)]
parent = [0] * (N+1)
for i in range(1, N+1):
  parent[i] = i

def find(a):
  if a == parent[a]:
    return a
  else:
    parent[a] = find(parent[a])
    return parent[a]

def union(a,b):
  a = find(a)
  b = find(b)
  if a != b:
    parent[b] = a

def checkSame(a,b):
  a = find(a)
  b = find(b)
  if a == b:
    return True
  else:
    return False

# 파티데이터 저장
for i in range(M):
  party[i] = list(map(int, input().split()))
  del party[i][0]

for i in range(M): # 각 파티에 참여한 사람들을 1개의 그룹으로 만들기
  firstPeople = party[i][0]
  for j in range(1, len(party[i])):
    union(firstPeople, party[i][j])

for i in range(M):
  isPossible = True
  firstPeople = party[i][0]
  for j in range(len(trueP)):
    if find(firstPeople) == find(trueP[j]):
      isPossible = False
      break
  if isPossible:
    result += 1

print(result)