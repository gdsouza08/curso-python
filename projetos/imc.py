nome = input("Digite seu nome: ")
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso / (altura * altura)

print("Bem vindo", nome, ", Seu IMC é ", imc)