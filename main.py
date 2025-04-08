
def maiornumero (a,b): 
    return a if a>b else b
    
def soma_recursiva(n):
    if n <= 1:
        return n
    return n + soma_recursiva(n - 1)
    
    
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))


print("O maior número é:", maiornumero(numero1, numero2))

n = int(input("Digite um número para somar de 1 até ele: "))

print("Soma de 1 até", n, "é:", soma_recursiva(n)) 

""" ou
 soma = 0
for i in range(1, n + 1):
    soma += i
    print(f"Somando {i}: total até agora = {soma}")

print("Soma final de 1 até", n, "é:", soma) """

