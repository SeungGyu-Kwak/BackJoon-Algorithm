import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

s, e = map(int, input().split())

ary = []
for i in range(1, e+1):
    for j in range(i):
        ary.append(i)
print(sum(ary[s-1:e]))