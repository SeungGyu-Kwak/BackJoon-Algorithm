# 트리 순회
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input()) # 노드의 개수
tree = {} # 딕셔너리로 저장
for i in range(N):
  root, left, right = input().split()
  tree[root] = [left, right]

# 전위 순회 구현
def preorder(n):
  if n == '.':
    return
  print(n, end='')
  preorder(tree[n][0]) # 왼쪽 탐색
  preorder(tree[n][1]) # 오른쪽 탐색

# 중위 순회 구현
def inorder(n):
  if n == '.':
    return
  inorder(tree[n][0]) # 왼쪽 탐색
  print(n, end='')
  inorder(tree[n][1]) # 오른쪽 탐색

# 후위 순회 구현
def postorder(n):
  if n == '.':
    return
  postorder(tree[n][0]) # 왼쪽 탐색
  postorder(tree[n][1]) # 오른쪽 탐색
  print(n , end = '')

preorder('A')
print()
inorder('A')
print()
postorder('A')