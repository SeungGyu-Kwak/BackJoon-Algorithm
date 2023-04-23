import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

DP = [[0 for _ in range(15)] for _ in range(15)]

#초기화하기
for i in range(0, 15):
    DP[0][i] = i
    DP[i][1] = 1

for i in range(1, 15):
    for j in range(2, 15):
        DP[i][j] = DP[i][j-1] + DP[i-1][j]

question = int(input()) # 질의 개수
for _ in range(question):
    k = int(input())
    n = int(input())
    print(DP[k][n])
    