n = 5
tblmul = [[i * j for j in range (n)] for i in range (n)]
print(*tblmul, sep='\n')