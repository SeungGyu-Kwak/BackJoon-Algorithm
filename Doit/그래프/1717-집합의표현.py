# 집합의 표현
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
sys.setrecursionlimit(100000)


N, M = map(int, input().split())
parent = [0] * (N+1)

def find(a): # find 연산 메소드
  if a == parent[a]:
    return a
  else:
    parent[a] = find(parent[a]) # 루트노드를 찾았으면 바로 parent[a]의 부모를 루트노드로 바꿔줌
    return parent[a]

def union(a, b):
  a = find(a)
  b = find(b)
  if a != b:
    parent[b] = a

def checkSame(a, b):
  a = find(a)
  b = find(b)
  if a == b:
    return True
  return False

for i in range(0, N+1):
  parent[i] = i

for i in range(M):
  question, a, b = map(int, input().split())
  if question == 0:
    union(a,b)
  else:
    if checkSame(a, b):
      print('YES')
    else:
      print('NO')