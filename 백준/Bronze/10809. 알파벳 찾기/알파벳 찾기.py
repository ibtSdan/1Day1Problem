s = input()
lst = [chr(c) for c in range(97,123)]
for c in lst:
  print(s.index(c) if c in s else -1,end=" ")