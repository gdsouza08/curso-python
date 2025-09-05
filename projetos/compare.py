valor1 = input("Digite o primeiro valor: ")
valor2 = input("Digite o segundo valor: ")

if valor1 > valor2:
    print("Primeiro valor", valor1, "maior que segundo valor", valor2)
elif valor1 == valor2:
    print("Os valores são iguais.")
elif valor1 < valor2:
    print("Primeiro valor", valor1, "menor que segundo valor", valor2)
else:
    print("Não foi possível fazer a comparação!")