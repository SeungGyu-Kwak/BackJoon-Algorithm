import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
S = int(input())
ary = list(map(int, input().split()))
ary.sort()
start_idx = 0
end_idx = len(ary)-1
count = 0

while start_idx < end_idx:
  tmp = ary[start_idx] + ary[end_idx]
  if tmp < S:
    start_idx += 1
  elif tmp > S:
    end_idx -= 1
  else:
    count += 1
    start_idx += 1
    end_idx -= 1

print(count)