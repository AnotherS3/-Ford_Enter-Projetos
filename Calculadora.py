#base da calculadora 1



#----------------------------------------------------------
#variaveis
nota1 = 0
nota2 = 0
soma = nota1+nota2
subtracao = nota1-nota2
divisao = nota1/nota2
multiplicacao = nota1*nota2
resto = nota1%nota2
expoente = nota1**nota2
nota1 = 0
nota2 = 0
opcao = int(input("===Digite o numero da opção desejada===/n" \
"1. Adição" \
"2. Subtração" \
"3. Divisão" \
"4. Multiplicação" \
"5. Restante da Divisão" \
"6. Expoente"))

if (opcao == 1):
    nota1 = float(input("Digite o primeiro numero"))
    nota2 = float(input("Digite o segundo numero"))
    print(f"{nota1}+{nota2} = {(nota1+nota2)}")
elif  (opcao == 2):
    nota1 = float(input("Digite o primeiro numero"))
    nota2 = float(input("Digite o segundo numero"))
    print(f"{nota1}-{nota2} = {(nota1-nota2)}")
elif (opcao == 3):
    nota1 = float(input("Digite o primeiro numero"))
    nota2 = float(input("Digite o segundo numero"))
    print(f"{nota1}/{nota2} = {(nota1/nota2)}")
elif (opcao == 4):
    nota1 = float(input("Digite o primeiro numero"))
    nota2 = float(input("Digite o segundo numero"))
    print(f"{nota1}*{nota2} = {(nota1*nota2)}")
elif (opcao == 5):
    nota1 = float(input("Digite o primeiro numero"))
    nota2 = float(input("Digite o segundo numero"))
    print(f"{nota1}%{nota2} = {(nota1%nota2)}")
elif (opcao == 6):
    nota1 = float(input("Digite o primeiro numero"))
    nota2 = float(input("Digite o segundo numero"))
    print(f"{nota1}**{nota2} = {(nota1**nota2)}")



#--------------------------------------------------------#

print(f"{nota1}+{nota2} = {(soma)}")
print(f"{nota1}-{nota2} = {(subtracao)}")
print(f"{nota1}/{nota2} = {(divisao)}")
print(f"{nota1}*{nota2} = {(multiplicacao)}")
print(f"{nota1}%{nota2} = {(resto)}")
print(f"{nota1}**{nota2} = {(expoente)}")

#--------------------------------------------------------#
