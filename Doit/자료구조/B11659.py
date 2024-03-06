import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = list(map(int, input().split()))

s = [0]
tmp = 0
for i in numbers:
  tmp = tmp + i
  s.append(tmp)

for i in range(M):
  startIdx, endIdx = map(int, input().split())
  print(s[endIdx] - s[startIdx-1])