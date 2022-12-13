# ATM
import sys
sys.stdin = open("input.txt", "r")

N = int(input())
p = list(map(int, input().split()))
p.sort()

time = 0
for i in range(0, len(p)):
  tmp = 0
  for j in range(0, i+1):
    tmp += p[j]
  time += tmp

print(time)

