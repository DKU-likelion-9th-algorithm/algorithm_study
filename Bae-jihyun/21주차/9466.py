import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def dfs(x):
    global result
    vis[x] = True
    cycle.append(x)
    num = arr[x]

    if vis[num]:    # 이미 방문한 정점 중
        if num in cycle:  # 다음 정점이 cycle list에 있다면 cycle이 형성된 것
            result += cycle[cycle[cycle.index(num)]:]  # 형성된 cycle 정점들을 result에 저장
        return              # 한 cycle을 찾았으면 return
    else:           # 방문을 안 해도 한 정점마다 이미 다음 정점을 선택했기 때문에
        dfs(num)    # dfs 진행


T = int(input())

for _ in range(T):
    n = int(input())
    arr = [0] + list(map(int, input().split()))
    vis = [False] * (n + 1)
    result = []

    for i in range(1, n + 1):
        if not vis[i]:    # 한번 방문한 정점은 다시 방문하지 않도록 한다.
            cycle = []    # 한 개의 연결을 담는 list
            dfs(i)

    print(n - len(result))

'''
result를 set으로 설정?
=> 한 학생당 한 명의 학생을 선택하기 때문에 result에 같은 정점이 두번 들어올 수 없다.
따라서 result는 중복을 없애주는 set이 아니어도 된다.

result += [cycle[cycle.index(num)]:] 인 이유
실제로 cycle이라면 cycle 리스트를 돌다가 결국 처음 cycle 시작 정점으로 돌아오기 때문에 
    cycle 리스트의 처음 인덱스부터 끝 인덱스까지 전부를 result에 저장
실제로 cycle이 아니라면 자기 자신을 선택했을 때이기 때문에 
    본인 정점부터 cycle 리스트 끝까지 = 본인만 저장
'''