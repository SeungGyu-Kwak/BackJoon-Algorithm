# 약수구하기
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N, K = map(int, input().split())
arr = [] # 약수 담을 리스트
for i in range(1, N+1):
    if N % i == 0:
        arr.append(i)

if len(arr) < K:
    print(0)
else:
    print(arr[K-1])