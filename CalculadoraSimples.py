# Calculadora simples em Python by zPhazeDeveloper
import time

numero1 = int(input("Digite o primeiro numero: "))
numero2 = int(input("Digite o segundo numero: "))
print("Opções de operações: +, -, *, ** ")

while True:
    operacao = input("Digite uma das opções acima: ")
    
    # Condições
    if operacao == "+":
        resultado = numero1 + numero2
        break  
    elif operacao == "-":
        resultado = numero1 - numero2
        break 
    elif operacao == "*":
        resultado = numero1 * numero2
        break  
    elif operacao == "**":
        resultado = numero1 ** numero2
        break  
    else:
        print("Essa conta é impossível")
print("Calculando resultado...")
time.sleep(1)

print("Pronto!")
print("O resultado é: ", resultado)
