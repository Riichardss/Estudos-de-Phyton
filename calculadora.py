print('Hello world')

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = (n1+n2)/2

print(f'sua media de {n1} e {n2} é {media}')

if media >= 7:
    print('Aprovado')

elif media >= 5 and media <= 6:
    print('Recuperação')

else:
    print('Reprovado')

    # media dos alunos e informar se foi aprovado, esta de recuperação ou foi reprovado.
