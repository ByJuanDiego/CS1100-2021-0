print("Input:")
n1 = str(input())
n2 = str(input())
n1 = n1.lower()
n2 = n2.lower()

score = 0       # El Love Match Score
vocales_n1 = 0  # Vocales del primer nombre
vocales_n2 = 0  # Vocales del segundo nombre

# Primera condicion:
for char in n1:
    if char in "aeiou": vocales_n1 += 1

for char in n2:
    if char in "aeiou": vocales_n2 += 1

if vocales_n1 == vocales_n2: score += 5

# Segunda condicion:
if (n1[0] in "love") and (n2[0] in "love"): score += 3

# Tercera condicion:
if (len(n1) >= 7) and (len(n2) >= 7): score += 2

print("Output: {}".format(score))
