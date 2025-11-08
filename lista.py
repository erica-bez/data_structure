# Criando uma lista
frutas = ['maçã', 'banana', 'laranja']

# Acessando um elemento (posição 0)
# Adicionando elemento
frutas.append('abacaxi')
frutas[2] = 'limao'
frutas.insert(2, 'uva')   # 0 é o índice da primeira posição
print(type(frutas))

print(frutas[3])

print(f'a quantidade é  {len(frutas)}')


# Removendo elemento
# frutas.remove('banana')
del frutas[1]
frutas.pop(2) 

# Alterando valor
#frutas[1] = 'manga'

print(frutas)
# Saída: ['maçã', 'manga', 'uva']
