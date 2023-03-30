# LCS 문제 2

import sys
sys.setrecursionlimit(10**6)
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

A = list(input())
A.pop() # \n 제거
B = list(input())
B.pop()

DP = [[0 for _ in range(len(B)+1)] for _ in range(len(A)+1)]
Path = [] # LCS 저장 리스트

for i in range(1, len(A)+1):
  for j in range(1, len(B)+1):
    if A[i-1] == B[j-1]:
      # 같은 문자열일 때
      DP[i][j] = DP[i-1][j-1] + 1 # 왼쪽 대각선 값 + 1
    else:
      # 다르면 왼쪽과 위 쪽의 값 중 큰 수
      DP[i][j] = max(DP[i-1][j], DP[i][j-1])

print(DP[len(A)][len(B)])

def getText(r, c):
  if r == 0 or c == 0:
    return
  if A[r-1] == B[c-1]: # 같으면 LCS에 기록하고 왼쪽 위로 이동
    Path.append(A[r-1])
    getText(r-1, c-1)
  else:
    if DP[r-1][c] > DP[r][c-1]:
      getText(r-1, c)
    else:
      getText(r, c-1)

getText(len(A), len(B))
for i in range(len(Path)-1, -1, -1):
  print(Path.pop(i), end='')