from collections import deque
import sys

dq = deque()

n = int(sys.stdin.readline())
size = 0

for i in range(n):
    w = sys.stdin.readline().split()  # 문자열 받을때는 str
    if w[0] == "push":
        dq.append(w[1])
        size += 1
    elif w[0] == "pop":
        if size > 0:
            pop = dq.pop()
            size -= 1
            print(pop)
        else:
            print(-1)
    elif w[0] == "size":
        print(size)
    elif w[0] == "empty":
        if size == 0:
            print(1)
        else:
            print(0)
    if w[0] == "top":
        if size > 0:
            top = dq.pop()
            print(top)
            dq.append(top)
        else:
            print(-1)
