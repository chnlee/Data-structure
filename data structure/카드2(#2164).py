# import queue

# normalQueue = queue.Queue()

# A = int(input())

# for i in range(1,A+1):
#   normalQueue.put(i)
# while True:
#   if normalQueue.qsize() == 1:
#     print(normalQueue.get())
#   normalQueue.get()
#   A = normalQueue.get()
#   normalQueue.put(A)

# #알고리즘
# 1. 1버리기 
# 2. 2줍기
# 3. 3버리기
# 4. 4줍기 
  
from collections import deque

dq = deque()

A = int(input())

for i in range(1,A+1):
  dq.append(i)

while len(dq) >1:
  dq.popleft()
  dq.rotate(-1)

print(dq[0])
