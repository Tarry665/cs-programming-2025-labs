lst = [1,2,3,4,5,6,7,8,3,10]
for i in range(len(lst)):
  if lst[i] == 3:
    lst[i] = 30
print(lst)