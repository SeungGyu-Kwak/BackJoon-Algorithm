import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    ary = list(map(int, input().split()))
    ary.sort(reverse = True)
    print(ary[2])