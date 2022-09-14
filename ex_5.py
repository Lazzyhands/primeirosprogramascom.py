#Exercício 4.5
distância = float(input("Digite a distância que você quer percorrer em Km: "))
if distância <= 200:
    preço = (distância* 0.50)
    print(f" O valor da viagem é: R${preço:5.2f}")
if distância > 200:
    preço = (distância* 0.45)
    print(f"O valor da viagem é: R${preço:5.2f}")
    
