import queue

normalQueue = queue.Queue() 
#큐생성(FIFO)

for i in range(5):
  normalQueue.put(i)
#큐에 item 넣기

while normalQueue.qsize():
  print(normalQueue.get())
#qzise() : 큐의 대략적인 크기를 돌려줌
#get() : 큐에서 항목을 제거하라고 반환함

if normalQueue.empty():
  print("Queue is empty")

#empty(): 비어있으면 True, 있으면 False


from collections import deque

dq = deque("1234")

dq.append("5")

dq.rotate(1) #1번 회전하게함
#{5,1,2,3,4}

while(len(dq)): #5
  print(dq[0])
  dq.popleft() #왼쪽에서부터 제거함

  