nomes = []
telefones = []
emails = []
print("\n\n =========== CADASTRO DE CONTATOS ============")

while True:
    nome = input("Informe o nome do seu contato:  (0  - finaliza): ")
    if nome == "0":
        break
    nomes.append(nome)  # adiciona na lista de nomes
    telefones.append(input("Infome o TELEFONE do seu contato: "))
    emails.append(input("Informe o Email do seu contato: "))

    print("\n\n =============== PESQUISANDO CONTATO CADASTRADO =============== ")
    buscaNome = input("\nInforme o nome para pesquisar: ")
    achou = False
    for i in range(len(nomes)):
        if nomes[i] == nome:
            print(nomes[i])
            print(telefones[i])
            print(emails[i])
            flag = achou
            break
        else:
            achou = False
    if achou == False:
        print("contato não localizado")
