# Criando um dicionário
pessoa = {
    'nome': 'Erica',
    'idade': 25,
    'cidade': 'Recife'
}

# Acessando valor pela chave
print(pessoa['nome'])  # Erica

# Adicionando nova chave
pessoa['profissão'] = 'Programadora'

# Alterando valor
pessoa['idade'] = 26

# Removendo chave
# del pessoa['cidade']
pessoa.pop('cidade')

print(len(pessoa))
pessoa['estado'] = 'ceara'
pessoa['telefone'] = 98765432
pessoa[987] = 'x=y'
del pessoa[987]
print(pessoa)
# Saída: {'nome': 'Erica', 'idade': 26, 'profissão': 'Programadora'}
