nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

print('*' * 50)
if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')

    if ' ' in nome:
        print("Seu nome contém espaços!")
    else:
        print("Seu nome NÃO contém espaços!")

    print(f'seu nome tem {len(nome)} letras')     
    print(f'A primeira letra do seu nome é: {nome[0]}')
    print(f'A última letra do seu nome é: {nome[-1]}')
else: 
    print("Nome e Idade devem ser informados!")
print('*' * 50)