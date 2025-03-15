# Calculadora simples em Python by zPhazeDeveloper
while True:
    num1 = input('🔢 Digite um numero: ')
    num2 = input('🔢 Digite o segundo numero: ')
    print('🧮 opções dos operadores: (+, -, *, /, **, //, %)')
    operador = input(f'🤔 Qual operador você deseja usar para calcular {num1} com {num2}: ')

    resultado = None

    ver1 = isinstance(num1, str)
    ver2 = isinstance(num2, str)

    if ver1 == True:
        num1 = int(num1)
    if ver2 == True:
        num2 = int(num2)

    if operador == '+':
        resultado = num1 + num2
    elif operador == '-':
        resultado = num1 - num2
    elif operador == '*':
        resultado = num1 * num2
    elif operador == '/':
        resultado = num1 / num2
    elif operador == '**':
        resultado = num1 ** num2
    elif operador == '//':
        resultado = num1 // num2
    elif operador == '%':
        resultado = num1 % num2
    else:
        print("Nenhuma das opções abaixo foi digitada, tente denovo!")

    print(f'🎉 O resultado da operação de {num1} {operador} {num2}: {resultado} ✨')
