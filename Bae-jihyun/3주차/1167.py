from collections import deque

v = int(input())

graph = [[] for _ in range(v + 1)]

for _ in range(v):
    temp = list(map(int, input().split()))
    for i in range(1, len(temp) - 1, 2):
        graph[temp[0]].append((temp[i], temp[i + 1]))


def bfs(idx):
    visited = [-1] * (v + 1)  # 방문 안 하면 -1, 방문하면 idx와의 거리
    queue = deque()
    queue.append(idx)  # 방문 할 노드들(정점(숫자)만 들어감)
    visited[idx] = 0

    result = [0, 0]  # 최대 길이, 가장 먼 정점

    while queue:
        old = queue.popleft()  # 지금 방문할 정점
        for new in graph[old]:  # old와 연결된 정점들을 돌아가며 idx와의 거리 갱신하기
            if visited[new[0]] == -1:  # 방문한적이 없다면

                # visited[old] : idx~old 정점까지 거리, new[1]:old~new까지 거리
                visited[new[0]] = visited[old] + new[1]
                queue.append(new[0])

                # idx~old 까지 길이보다 old+old~new까지의 길이가 길다면
                if result[0] < visited[new[0]]:
                    result[0] = visited[new[0]]  # 최대길이에 old+old~new길이를 넣어주고
                    result[1] = new[0]  # 정점에 new를 넣어준다.
    return result


value, node = bfs(1)  # 정점 1을 기준으로 가장 먼곳을 구하고
answer, node2 = bfs(node)  # 이 가장 먼 정점을기준으로 다시 한번 수행
print(answer)

'''
1인 정점을 기준으로 가장 먼곳을 구하고,
이 가장 먼 정점을 기준으로 다시 한번 수행해야한다.
https://blog.myungwoo.kr/112
'''

"""
피드백 코멘트 :
트리의 지름에 대해 배울 수 있는 좋은 경험이 되셨으리라 생각합니다.
깔끔하게 잘 푸신 것 같습니다. 고생하셨습니다!
"""
