from random import *

num_digitos = 6
contra = ""
for digitos in range(num_digitos):
    contra += str(randint(0, 9))
print(contra)
