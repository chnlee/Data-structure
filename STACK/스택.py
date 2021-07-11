# #Stack
import sys
N = int(sys.stdin.readline())
# global _list 
_list = []
# def push_stack(number):
#   _list.append(number)
#   print(_list)
# def pop_stack():
#   if len(_list) == 0:
#     print(_list)
#     print(-1)
#   else:
#     print(_list.pop)
# def size_stack():
#   print(_list)
#   print(len(_list))
# def empty_stack():
#   if len(_list) == 0:
#     print(_list)
#     print(1)
#   else:
#     print(_list) 
#     print(0)
# def top_stack():
#   if len(_list) == 0:
#     print(_list)
#     print(-1)
#   else:
#     print(_list)
#     print(_list[len(_list)-1])

for _ in range(N):
  command = sys.stdin.readline()
  if("push" in command):
    _list.append(int(command[5:-1]))
  elif("pop" in command):
    if (len(_list) == 0):
      print(-1)
    else:
      print(_list.pop())
  elif("size" in command):
    print(len(_list))
  elif("empty" in command):
    if len(_list) == 0:
     print(1)
    else: 
     print(0)
  elif("top" in command):
    if len(_list) == 0:
     print(-1)
    else:
     print(_list[len(_list)-1])


      


