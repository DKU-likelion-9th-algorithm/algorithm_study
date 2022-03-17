import sys
input = sys.stdin.readline


class Node(object):
    def __init__(self, key, data = None):
        self.key = key
        self.data = data
        self.child = {}


class Trie(object):
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        curr_node = self.head

        # 삽입할 string 각각 문자에 대해 자식 Node를 만들며 내려간다.
        for char in string:
            # 자식 Node 중에 같은 문자가 없으면 Node를 새로 생성하고 부모의 child에 넣어준다.
            if char not in curr_node.child:
                curr_node.child[char] = Node(char)
            curr_node = curr_node.child[char]  # 같은 문자가 있다면 해당 노드로 이동

        # 문자열의 끝임을 알려주기 위해 data 필드에 문자열 전체를 넣어준다.
        curr_node.data = string

    def search(self, string):
        curr_node = self.head

        # 문자열의 끝을 찾기
        for char in string:
            curr_node = curr_node.child[char]

        # 문자열의 끝인데 child가 있다면 전화번호 일관성이 없다.
        if curr_node.child:
            return True  # 일관성 없음
        else:
            return False  # 일관성 있음


T = int(input())
for _ in range(T):
    N = int(input())
    trie = Trie()
    nums = []
    flag = True

    for _ in range(N):
        num = input().rstrip()
        nums.append(num)
        trie.insert(num)

    nums.sort()   # 정렬까지 해주면 바로 뒤 문자열과만 비교해주면 된다.

    for num in nums:
        if trie.search(num):  # 일관성 없음
            flag = False
            break

    if flag:
        print("YES")
    else:
        print("NO")


'''
num을 input()만 해주면 nums는 ['911\n', '97625999\n', '91125426\n']로 들어오게 된다.
input().rstrip()을 해주면 nums가 제대로 채워지고 알맞게 동작한다.

원래 search는 아래와 같다.
def search(self, string):
        curr_node = self.head

        for char in string:
            if char in curr_node.children:   # 자식노드에 char가 있다면
                curr_node = curr_node.children[char]  # 자식노드로 이동
            else:                            # 없다면
                return False                 # 같은 문자열이 없음.

        if curr_node.data != None:           # 마지막 노드까지 왔을 때 data가 None이 아니라면(문자열의 끝이다.)
            return True                      # 같은 문자열이 있음.
'''