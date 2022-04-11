class Solution:
    def transform(self, stringToTransform):
        texto = ""
        for char in stringToTransform: texto += str(format(ord(char), "08b"))
        return texto

stringToTransform = str(input("Ingresa la cadena a convertir a binario: "))
print(f"Su traduccion en binario es: {Solution().transform(stringToTransform)}")
