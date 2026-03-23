#ESTADO CIVIL DO USUARIO

estado_civil = input("Digite seu estado civil usando letras Exemplo: \n (S) para solteiro \n (C) para casado \n (V) para viuvo  \n (D) para divorciado \n (O) para outros \n Digite aqui: ")

#--------------------------------------------------------------
if estado_civil == "S" or estado_civil == "s":
    print("Você é solteiro")
elif estado_civil == "C" or estado_civil == "c":
    print("Você é casado")
elif estado_civil == "V" or estado_civil == "v":
    print("Você é viuvo")
elif estado_civil == "D" or estado_civil == "d":
    print("Você é divorciado")
elif estado_civil == "O" or estado_civil == "o":
    print("Você é outros")
else:
    print("Você digitou um estado civil invalido")
#-------------------------------------------------------------
