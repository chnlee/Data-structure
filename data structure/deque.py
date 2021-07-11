from collections import deque

dq = deque()
dq = deque('12345')

dq.append(6)
dq.appendlef(0)

removed = dq.pop()
print(removed) #012345
removed = dq.popleft
print(removed) #12345

dq.rotate(1) #51234
dq.rotate(-2) #23451