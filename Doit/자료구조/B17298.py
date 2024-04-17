import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
ary = list(map(int, input().split()))
answer = [0] * N
st = [] # 스택
st.append(0) # 첫번째는 무조건 비어있음.

for i in range(1, N):
  while st and ary[st[-1]] < ary[i]:
    idx = st.pop() # 해당 인덱스를 pop한다.
    answer[idx] = ary[i]
  st.append(i)

while st:
  idx = st.pop()
  answer[idx] = -1

print(*answer)