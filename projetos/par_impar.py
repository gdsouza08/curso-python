entrada = input("Digite um número: ")

if entrada.isdigit():
    entrada_int = int(entrada)
    par_impar = entrada_int % 2 == 0
    print("O número digitado é PAR")
elif entrada.isdigit():
    entrada_int = int(entrada)
    par_impar = entrada_int % 2 != 0
    print("O número digitado é ÍMPAR")
else:
    print("O número digitado não é um valor inteiro!")