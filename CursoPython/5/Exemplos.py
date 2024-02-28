# Função Simples:

def saudacao(nome):
    return f"Olá, {nome}!"
# Função com Parâmetros Padrão:

def potencia(base, expoente=2):
    return base ** expoente
# Função com Retorno Múltiplo:

def opera_numeros(a, b):
    soma = a + b
    diferenca = a - b
    return soma, diferenca

def calcular_quadrado(numero):
    return numero ** 2

resultado = calcular_quadrado(5)
print(resultado)  # Saída: 25

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

resultado = fatorial(5)
print(resultado)  # Saída: 120


# estatisticas.py

def calcular_media(lista_numeros):
    return sum(lista_numeros) / len(lista_numeros)

def calcular_mediana(lista_numeros):
    lista_ordenada = sorted(lista_numeros)
    tamanho = len(lista_numeros)
    if tamanho % 2 == 0:
        meio1 = lista_ordenada[tamanho // 2 - 1]
        meio2 = lista_ordenada[tamanho // 2]
        return (meio1 + meio2) / 2
    else:
        return lista_ordenada[tamanho // 2]

# manipulacao_strings.py

def inverter_string(texto):
    return texto[::-1]

def contar_caracteres(texto):
    return len(texto)
# E podemos utilizar essas funções em nosso programa principal:


import manipulacao_strings

frase = "Python é incrível!"
frase_invertida = manipulacao_strings.inverter_string(frase)
quantidade_caracteres = manipulacao_strings.contar_caracteres(frase)

