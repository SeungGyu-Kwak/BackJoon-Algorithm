import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

F = [0] * 21 # 자리별로 만들 수 있는 경우의 수 저장하는 리스트
S = [0] * 21 # 순열 담는 리스트
visited = [False] * 21 # 숫자 사용여부 리스트

N = int(input()) # 순열의 길이
F[0] = 1
# 자리별로 만들 수 있는 경우의 수로 초기화
for i in range(1, N+1):
    F[i] = F[i-1] * i
    
inputList = list(map(int, input().split()))

# 1번 문제에 해당
if inputList[0] == 1:
    K = inputList[1]
    for i in range(1, N+1):
        cnt = 1
        for j in range(1, N+1):
            if visited[j]: #이미 사용한 숫자는 사용 못함
                continue
            if K <= cnt * F[N-i]:
                K -= (cnt-1) * F[N-1]
                S[i] = j
                visited[j] = True
                break
            cnt+=1 
    for i in range(1, N+1):
        print(S[i], end = " ")
else:
    K = 1
    for i in range(1, N+1):
        cnt = 0
        for j in range(1, inputList[i]):
            if not visited[j]:
                cnt += 1
        K += cnt * F[N-i]
        visited[inputList[i]] = True
    
    print(K)