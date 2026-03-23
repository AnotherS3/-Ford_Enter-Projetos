n1 = float(input("Digite a primeira nota"))
n2 = float(input("Digite a segunda nota"))
n3 = float(input("Digite a terceira nota"))
media = (n1+n2+n3)/3

if (media >= 7):
    print("Passou de ano Bonitão (Aprovado)")

elif(media >= 5):
    print("Quem passa direto é trem!!!! (Recuperação)")

else: 
    print("Perdeu Otário (Reprovado)")