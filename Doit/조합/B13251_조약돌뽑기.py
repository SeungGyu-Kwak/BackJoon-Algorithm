import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

M = int(input()) # 색상 개수
list1 = list(map(int, input().split()))
totalCnt = sum(list1) # 조약돌 전체 개수

K = int(input())

probability = [0] * 51
answer = 0
for i in range(M):
    if list1[i] >= K:
        probability[i] = 1
        for j in range(K):
          probability[i] = probability[i] * (list1[i] - j) / (totalCnt - j)
        answer += probability[i]

print(answer)
