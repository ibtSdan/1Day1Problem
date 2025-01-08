n = input()
count = 0

if int(n)<10:
  n = '0'+n
new = n

while True:
  count += 1
  nn = str(int(new[0]) + int(new[1]))
  new = new[-1]+nn[-1]
  if n==new:
    break

print(count)