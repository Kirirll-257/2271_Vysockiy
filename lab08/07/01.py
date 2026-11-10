x = [int(t) for t in input().split()]
for i in x:
     if i < 0:
        print("Found negative: ", i)
        break
else:
     print("All numbers are non-negative")