def adicionar_tarefa(lista, tarefa):
    lista.append(tarefa)
    print("Tarefa adicionada com sucesso!")

def remover_tarefa(lista, indice):
    if indice < len(lista):
        del lista[indice]
        print("Tarefa removida com sucesso!")
    else:
        print("Índice inválido!")

def exibir_tarefas(lista):
    print("Lista de tarefas:")
    for i, tarefa in enumerate(lista):
        print(f"{i + 1}. {tarefa}")

def main():
    lista_de_tarefas = []

    while True:
        print("\n=== TO-DO LIST ===")
        print("1. Adicionar tarefa")
        print("2. Remover tarefa")
        print("3. Exibir tarefas")
        print("4. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            tarefa = input("Digite a nova tarefa: ")
            adicionar_tarefa(lista_de_tarefas, tarefa)
        elif escolha == "2":
            indice = int(input("Digite o índice da tarefa a ser removida: ")) - 1
            remover_tarefa(lista_de_tarefas, indice)
        elif escolha == "3":
            exibir_tarefas(lista_de_tarefas)
        elif escolha == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
