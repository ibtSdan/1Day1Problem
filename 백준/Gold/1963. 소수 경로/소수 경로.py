from collections import deque
lst = [i for i in range(10000)]
for i in range(2,int(9999**0.5)+1):
    if lst[i]==0:
        continue
    for j in range(i*2,10000,i):
        lst[j] = 0
test = int(input())
for _ in range(test):
   a, b = map(int, input().split())
   visited = [False]*(10000)
   dq = deque()
   dq.append((a,0))
   visited[a] = True
   check = False
   while dq:
      now, time = dq.popleft()
      if now==b:
          print(time)
          check = True
          break
      for i in range(10):
          new = int(str(i)+str(now)[1:])
          if 1000<=new<=9999 and lst[new] and not visited[new]:
              dq.append((new,time+1))
              visited[new] = True
      for i in range(10):
          new = int(str(now)[0]+str(i)+str(now)[2:])
          if 1000<=new<=9999 and lst[new] and not visited[new]:
              dq.append((new,time+1))
              visited[new] = True
      for i in range(10):
          new = int(str(now)[:2]+str(i)+str(now)[-1])
          if 1000<=new<=9999 and lst[new] and not visited[new]:
              dq.append((new,time+1))
              visited[new] = True
      for i in range(10):
          new = int(str(now)[:3]+str(i))
          if 1000<=new<=9999 and lst[new] and not visited[new]:
              dq.append((new,time+1))
              visited[new] = True
   if not check:
      print("Impossible")