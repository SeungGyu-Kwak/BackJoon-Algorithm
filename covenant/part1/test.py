import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N, *arr = map(int, input().split())
print(N)


A = [[0]*2 for _ in range(4)]
print(A)