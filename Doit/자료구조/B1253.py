import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
ary = list(map(int, input().split()))
ary.sort()
count = 0

for k in range(N):
  find = ary[k]
  start_idx = 0
  end_idx = N - 1
  
  while start_idx < end_idx:
    tmp = ary[start_idx] + ary[end_idx]
    if tmp < find:
      start_idx += 1
    elif tmp > find:
      end_idx -= 1
    else:
      if start_idx != k and end_idx != k:
        count += 1
        break
      elif start_idx == k:
        start_idx +=1
      else:
        end_idx -= 1

print(count)