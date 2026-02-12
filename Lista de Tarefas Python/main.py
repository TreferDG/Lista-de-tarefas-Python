import json

def salvar_tarefas(tarefas):
    with open("tarefas.json", "w", encoding="utf-8") as arquivo:
        json.dump(tarefas, arquivo, ensure_ascii=False, indent=4)

def carregar_tarefas():
    try:
        with open("tarefas.json", "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Lista de tarefas
tarefas = carregar_tarefas()

# Menu Interativo
while True:
    print("\n---Lista de Tarefas---")
    print("1 - Adicionar Tarefa")
    print("2 - Listar Tarefas")
    print("3 - Marcar Tarefa como concluída")
    print("4 - Remover Tarefa")
    print("5 - Sair")

    opcao = input("Selecione uma opção: ")

    # Adicionar tarefa
    if opcao == "1":
        nome = input("Digite sua tarefa: ")
        tarefa = {"nome": nome, "concluida": False}
        tarefas.append(tarefa)
        salvar_tarefas(tarefas)
        print("Sua tarefa foi adicionada com sucesso!")

    # Listar tarefas
    elif opcao == "2":
        if len(tarefas) == 0:
            print("Nenhuma tarefa cadastrada.")
        else:
            print("\nTarefas:")
            for i, t in enumerate(tarefas):
                status = "✔" if t["concluida"] else "✘"
                print(f"{i+1} - {t['nome']} [{status}]")

    # Marcar como concluída
    elif opcao == "3":
        if len(tarefas) == 0:
            print("Não há tarefas para concluir.")
        else:
            numero = int(input("Digite o número da tarefa concluída: "))
            if 1 <= numero <= len(tarefas):
                tarefas[numero - 1]["concluida"] = True
                salvar_tarefas(tarefas)
                print("Tarefa marcada como concluída!")
            else:
                print("Tarefa não encontrada.")

    # Remover tarefa
    elif opcao == "4":
        if len(tarefas) == 0:
            print("Não há tarefas para remover.")
        else:
            numero = int(input("Digite o número da tarefa para excluir: "))
            if 1 <= numero <= len(tarefas):
                tarefas.pop(numero - 1)
                salvar_tarefas(tarefas)
                print("Tarefa excluída com sucesso.")
            else:
                print("Tarefa não encontrada.")

    # Sair
    elif opcao == "5":
        print("Saindo...")
        break

    else:
        print("Opção inválida.")
