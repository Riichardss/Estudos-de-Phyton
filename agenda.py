# criar uma  agenda que receba as informações dos contatos: nome, e-mail, telefone, use listas e estrutura de repetição


def exibir_contatos(contatos):
    print("lista de contatos: ")
    for contato in contatos:
        print("Nome:", contato[0])
        print("Telefone:", contato[1])
        print("E-mail:", contato[2])
        print("--------------------")

# Função principal


def main():
    contatos = []  # Lista para armazenar os contatos

    while True:
        print("\n1. Adicionar Contato")
        print("2. Exibir Contatos")
        print("3. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Digite o nome do contato: ")
            telefone = input("Digite o telefone do contato: ")
            email = input("Digite o e-mail do contato: ")
            contatos.append([nome, telefone, email])
            print("Contato cadastrado com sucesso!")
        elif opcao == '2':
            exibir_contatos(contatos)
        elif opcao == '3':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()
