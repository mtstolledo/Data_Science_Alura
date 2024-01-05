#1 - Crie uma lista para cada informação a seguir:

'''Lista de números de 1 a 10;
   Lista com quatro nomes;
   Lista com o ano que você nasceu e o ano atual.'''
   
print("Resposta nº 1")

lista_de_numeros = [1,2,3,4,5,6,7,8,9,10] ; print(lista_de_numeros)
lista_de_nomes = ['mat','mel','bob','karl']; print(lista_de_nomes)
lista_de_anos = [2001,2023]; print(lista_de_anos)

print("############################")

#2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.

print("Resposta nº 2")


for lista in lista_de_numeros:
    print(int(lista), end=' ')
    
print("\n############################")


#3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.

print("Resposta nº 3")

lista_de_numeros = [1,2,3,4,5,6,7,8,9,10]
somalista = 0
total = 0
for lista in lista_de_numeros:
    
    if(lista % 2 == 0 ):
        
        print(f"A soma de {lista} e {somalista} é {lista + somalista} ")
        somalista = somalista + lista
print("############################")       

#4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente

print("Resposta nº 4")

for lista in reversed(lista_de_numeros):        
    print(int(lista), end=' ')
print("\n############################")    

'''5 - Solicite ao usuário um número e, em seguida, utilize um loop for 
    para imprimir a tabuada desse número, indo de 1 a 10.'''

print("Resposta nº 5")

numero = int(input("Digite um número inteiro"))
for num in range(1,11):
    print(f" {numero} * {num} = {numero * num} ")
print("############################")

'''6 - Crie uma lista de números e utilize um loop for para 
calcular a soma de todos os elementos. Utilize um bloco 
try-except para lidar com possíveis exceções.'''

print("Resposta nº 6")
lista_de_numeros = [1, 2, -3, 4, 5, 6, 7, 8, 9, 10]
resultado = 0

try:
    quantidade_elementos = int(input("Digite a quantidade de elementos que deseja adicionar à lista: "))
    lista_de_numeros = []

    for _ in range(quantidade_elementos):
        numero = int(input("Digite um número: "))
        lista_de_numeros.append(numero)

    resultado = sum(lista_de_numeros)
    print(f"A lista de números é: {lista_de_numeros}")
    print(f"A soma dos elementos da lista é: {resultado}")

except ValueError as e:
    print(f"Erro mateus : {e}")
    
'''7 - Construa um código que calcule a média dos valores em uma
lista. Utilize um bloco try-except para lidar com a divisão por zero,
caso a lista esteja vazia.'''  

print("Resposta nº 7")    
lista_de_numeros = [1, 2,  , 4, 5, 6, 7, 8, 9, 10]
media = 0
soma = 0

for lista in lista_de_numeros:
    
        try:
           soma +=  lista 
           media = soma / lista
           print(f"{soma} e {media:.2f}")
          
        except ZeroDivisionError:
            print("Oops! Não é possível dividir por 0.")

print(soma,media)

    
    
