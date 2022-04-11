avion = [[0, 1, 1, 1],
         [1, 1, 0, 1],
         [1, 1, 1, 0],
         [1, 0, 1, 0],
         [1, 0, 0, 1],
         [0, 1, 1, 1],
         [1, 1, 0, 0],
         [1, 0, 0, 0],
         [1, 1, 0, 0],
         [1, 1, 1, 0],
         [0, 0, 1, 0],
         [1, 1, 1, 0],
         [0, 0, 1, 0],
         [-1, -1, -1, -1],
         [-1, -1, -1, -1],
         [1, 0, 1, 0],
         [1, 0, 0, 1],
         [0, 1, 0, 1],
         [0, 1, 1, 0],
         [0, 1, 0, 0]]

disA = 0
disB = 0
disC = 0
disD = 0

for f in range(len(avion)):
    for c in range(len(avion[0])):
        print(avion[f][c], end=" ")
    print()
print('\nOutput: ')

for f in range(len(avion)):
    if avion[f][0] == 0: disA += 1
    elif avion[f][1] == 0: disB += 1
    elif avion[f][2] == 0: disC += 1
    elif avion[f][3] == 0: disD += 1

print(f"A){disA} {20-disA}\n"
      f"B){disB} {20-disB}\n"
      f"C){disC} {20-disC}\n"
      f"D){disD} {20-disD}")
