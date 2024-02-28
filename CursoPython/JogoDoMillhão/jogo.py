import random
from perguntas import perguntas

def exibir_pergunta(pergunta):
    print(pergunta["pergunta"])
    for opcao in pergunta["opcoes"]:
        print(opcao)
    resposta = input("Escolha a opção correta (a, b, c, d): ").strip().lower()
    return resposta

def verificar_resposta(pergunta, resposta):
    return resposta == pergunta["resposta"]

def jogar():
    dinheiro_acumulado = 0
    random.shuffle(perguntas)
    for pergunta in perguntas:
        resposta = exibir_pergunta(pergunta)
        if verificar_resposta(pergunta, resposta):
            print("Resposta correta!\n")
            dinheiro_acumulado += 1000
        else:
            print("Resposta incorreta!\n")
            print("Você perdeu! Sua pontuação final é:", dinheiro_acumulado)
            return
    print("Parabéns! Você acertou todas as perguntas e ganhou 1 milhão de reais!")

if __name__ == "__main__":
    print("Bem-vindo ao Quem Quer Ser um Milionário!\n")
    jogar()
