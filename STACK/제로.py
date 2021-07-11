a = int(input())
_list = []

for i in range(a):
  A = int(input())
  if A == 0 and len(_list)>=1:
    _list.pop()
  else: _list.append(A)

print(sum(_list))