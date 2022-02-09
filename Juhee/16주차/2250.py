"""
1. 열 번호가 주어지지 않는데 어떻게 알 수 있나 고민하다가 결국 검색
--> 중위 순회. 중위 순회 순서 = 열 번호
이걸 왜 생각 못했을까

2. 레벨을 구해야 한다.
https://knowable.tistory.com/32

"""
import sys

input = sys.stdin.readline

tree = {}


class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right
        self.parent = -1


def in_order(node, level):
    global column_cnt, depth
    depth = max(depth, level)
    if node.left != -1:
        in_order(tree[node.left], level + 1)
    # 각 level별로 최대값( level_max[] ) 최소값( level_min[])을 계속 저장해준다.
    level_min[level] = min(level_min[level], column_cnt)
    level_max[level] = max(level_max[level], column_cnt)
    column_cnt += 1
    if node.right != -1:
        in_order(tree[node.right], level + 1)


num = int(input())
startValue = 0
level_min = [num]
level_max = [0]
column_cnt = 1
depth = 1

for i in range(1, num + 1):
    tree[i] = Node(i, -1, -1)
    level_min.append(num)
    level_max.append(0)

for i in range(num):
    value, left, right = map(int, input().split())
    if i == 0:
        startValue = value
    tree[value].left = left
    tree[value].right = right
    if left != -1:
        tree[left].parent = value
    if right != -1:
        tree[right].parent = value

in_order(tree[startValue], 1)

result_width = -1
result_level = 0

for i in range(1, depth + 1):
    width = level_max[i] - level_min[i]
    if result_width < width:
        result_width = width
        result_level = i

print(result_level, result_width + 1)
