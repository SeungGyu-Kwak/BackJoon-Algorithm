# 문자열 집합
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split())
textList = set([input() for _ in range(N)])
count = 0

for _ in range(M):
  subText = input()
  if subText in textList:
    count += 1

print(count)