import sys
from collections import deque

n= int(sys.stdin.readline())

d = deque()
size = 0

for _ in range(n):
    w = list(map(str, sys.stdin.readline().split()))
    if w[0]=='push':
        size +=1
        d.append(w[1])
    elif w[0]=='front':
        if size==0:
            print(-1)
        else:
            a = d.popleft()
            print(a)
            d.appendleft(a)
    elif w[0]=='back':
        if size==0:
            print(-1)
        else:
            a = d.pop()
            print(a)
            d.append(a)
    elif w[0]=='pop':
        if size==0:
            print(-1)
        else:
            a = d.popleft()
            print(a)
            size -=1
    elif w[0]=='size':
        print(size)
    elif w[0] == 'empty':
        if size==0:
            print(1)
        else:
            print(0)




