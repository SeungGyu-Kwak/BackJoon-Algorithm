# 구간 합 구하기 4
# s[n] = s[n-1] + a[n]
import sys
input = sys.stdin.readline
sys.stdin = open('input.txt', 'r')

N, M = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))

# 합 배열 만들기
s = [0]
tmp = 0
for i in range(N):
  tmp += a[i]
  s.append(tmp)
  
for i in range(M):
  start, end = map(int, sys.stdin.readline().split())
  print(s[end] - s[start-1])