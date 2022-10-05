#Programa que calcula média de alunos

n1 = int(input("Digite a primeira nota:"))
n2 = int(input("Digite a segunda nota:"))
n3 = int(input("Digite a terceira nota:"))
média = (n1 + n2 + n3)/3
if média >= 7:
    print(f"Aprovado com média {média}")
if média < 7:
    print(f"Reprovado com média {média}")
