# 11725 - 트리의 부모 찾기
# 트리가 주어지고 루트노드를 1이라 할 때 2 ~ N번 노드의 부모 출력

# 1.무식하게 접근
# 입력 때마다 각 노드들에 연결된 노드들(부모 자식 상관X) 모두 표시
# 입력이 끝나면 1번은 어차피 루트라 부모 노드가 없으므로 1번의 자식들의 연결노드에서 1번을 지우고,
# 걔네들의 자식들에 대해서도 같은 행동을 해주면 됨

import sys

sys.setrecursionlimit(1000000)

input = sys.stdin.readline

N = int(input())

Tree = [[] for _ in range(N + 1)]
# 트리 입력받기
for _ in range(N - 1):
    n1, n2 = map(int, input().split())
    Tree[n1].append(n2)
    Tree[n2].append(n1)
# 정답배열 - 여기에 각 노드들의 부모를 저장
answer = [0 for _ in range(N + 1)]

# 순회할 노드와 부모노드를 받는 함수
def mapping_parent(node, parent):
    # 자신과 연결된 노드들을 순회
    for cnode in Tree[node]:
        # 순회중인 노드가 부모노드가 아니라면(= 자식노드인 경우) 
        if cnode != parent:
            # 내가 이 노드의 부모라는 뜻이 됨
            answer[cnode] = node
            mapping_parent(cnode, node)

mapping_parent(1, 0)

for i in range(2, N + 1):
    print(answer[i])


# 트리 or 그래프를 배열 형태와 딕셔너리 형태로 만드는 것
# 공통점 : 모든 노드에 대해 각 노드와 그에 연결된 노드들을 표현가능
# 차이점 : 딕셔너리는 키값이 노드의 값 역할을 하고 value가 연결된 노드들을 표현하게 되는 반면
#        배열 형태는 인덱스번호가 값 역할을 함

# 장단점?
# 딕셔너리 장점 : 노드들이 숫자가 아니라 문자 등일 때도 키로 표현가능
#             실제로 트리 / 그래프에 실존하는 노드들에 대한 정보만 가짐 
#        단점 : 값을 추가할 때는 일단 딕셔너리에 특정 키 값이 있는지 확인하는 작업을 거쳐야 함

# 배열 장점 : 값을 추가 할 때 따로 확인하는 작업 없이 직빵으로 가능
#     단점 : 노드들이 숫자가 아니라 문자 등이라면 불편해짐
#          트리/그래프에 실존하지 않는 노드들만 가지는 게 아님 -> 메모리 낭비




