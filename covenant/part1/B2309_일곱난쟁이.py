import sys
from itertools import combinations
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

ary = []
for i in range(9):
    num = int(input())
    ary.append(num)

result = list(combinations(ary, 7))
for v in result:
    if sum(v) == 100:
        for j in sorted(v): # 오름차순으로 정렬
            print(j)
        break