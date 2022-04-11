n = int(input("Input: "))
print("\nOutput: ")

for f in range(1, n+1):
    for c in range(1, n+1):
        if f+c==n+1 or f==c: print("* ", end="")
        else: print("  ", end="")
    print()
    
