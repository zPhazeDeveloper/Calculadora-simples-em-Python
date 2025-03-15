# Calculadora simples em Python by zPhazeDeveloper
while True:
    num1 = float(input('🔢 Digite um numero: '))
    num2 = float(input('🔢 Digite o segundo numero: '))
    print('🧮 opções dos operadores: (+, -, *, /, **, //, %)')
    operador = input(f'🤔 Qual operador você deseja usar para calcular {num1} com {num2}: ')

    resultado = None

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
    escolha = input('Escolha: Digite "1" para mostrar o resultado inteiro, Digite "2" para mostrar o resultado com casa decimais')
    if escolha == "1":
        print(f"print(f'🎉 O resultado da operação de {num1} {operador} {num2}: {int(resultado)} ✨')")
    elif escolha == "2":
        print(f"print(f'🎉 O resultado da operação de {num1} {operador} {num2}: {resultado} ✨')")
