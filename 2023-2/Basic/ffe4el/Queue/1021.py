import sys
from collections import deque

n, m = map(int, input().split())

want = list(map(int, input().split()))

d = deque()
q = deque()

for i in range(n):
    q.append(i+1)

for i in range(m):
    d.append(want[i])

cnt=0

for i in range(m):
    a = d.popleft()
    if a < (n//2):
        while True:
            b = q.popleft()
            if b==a:# 찾고자 하는 값 찾음
                break
            q.append(b)
            cnt+=1
    else:
        while True:
            b = q.pop()
            q.appendleft(b)
            cnt +=1
            if b==a:
                break

print(cnt)
