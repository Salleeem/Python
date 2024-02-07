#Operação com variáveis

salario = 3000
bonus = 500
salario_total = salario + bonus

#String
  
nome = "Maria"
sobrenome = "Silva"
nome_completo = nome + " " + sobrenome

#Atualização de variáveis

contador = 0
contador = contador + 1


#Variáveis em Estruturas de Controle:

idade = 18
if idade >= 18:
    pode_votar = True
else:
    pode_votar = False



print(pode_votar)


# Strings simples
nome = "Alice"
mensagem = 'Olá, seja bem-vindo!'

# Concatenação de strings
nome_completo = nome + " Wonderland"

# Formatação de strings
mensagem_formatada = f"Olá, {nome}! Você tem {idade} anos."

print(nome_completo + mensagem_formatada)


# Listas (mutáveis)
frutas = ["maçã", "banana", "uva"]
numeros = [1, 2, 3, 4, 5]

# Adicionando elementos a uma lista
frutas.append("laranja")



# Dicionário chave-valor
pessoa = {
    "nome": "Carlos",
    "idade": 30,
    "profissao": "engenheiro"
}

# Acessando valores
print(pessoa["nome"])
print(pessoa.get("idade"))

# Adicionando novo par chave-valor
pessoa["cidade"] = "São Paulo"




# Variáveis booleanas
tem_cafe = True
tem_cha = False

# Expressões booleanas
tem_bebida_quente = tem_cafe or tem_cha
tem_as_dois = tem_cafe and tem_cha




