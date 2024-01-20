'''1 - Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.'''
print("Resposta 1")
pessoa = {'nome':'Mateus','idade':23,'cidade':"São João"}
print(pessoa)
print("#"*50)

'''2 - Utilizando o dicionário criado no item 1:'''
'''     Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa)
        Adicione um campo de profissão para essa pessoa;
        Remova um item do dicionário.'''
print("Resposta 2")
pessoa['idade'] = 22
pessoa['Profissão'] = "Desenvolvedor Python"
pessoa.pop("nome")
print(pessoa)
print("#"*50)

'''3 - Crie um dicionário para representar números e seus quadrados de 1 a 5.'''
print("Resposta 3")
numeros_quadrados = {x: x**2 for x in range(1, 6)}
print(numeros_quadrados)
print("#"*50)

'''4 - Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário.'''
print("Resposta 4")
dicionario = numeros_quadrados
chave_procurada = 3
if chave_procurada in dicionario:
    print(f"A chave {chave_procurada} existe no dicionário. Valor : {dicionario[chave_procurada]}")
else:
    print("A chave x não existe no dicionário.")
print("#"*50)

'''5 - Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário.'''
print("Resposta 5")
frase = "Botafogo, Botafogo, campeão !"
contagem_palavras = {}
palavras = frase.split()
for palavra in palavras:
    contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1
print(contagem_palavras)



