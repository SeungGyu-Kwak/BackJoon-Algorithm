import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

T = int(input()) # 테스트케이스 개수
for _ in range(T):
    N = int(input())
    binary = bin(N)
    arr = list(map(int,binary[2:]))
    
    idx = 0
    for i in range(len(arr)-1, -1, -1):
        if arr[i] == 1:
            print(idx, end=" ")
        idx += 1