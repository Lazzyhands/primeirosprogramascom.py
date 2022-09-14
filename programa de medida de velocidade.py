velocidade = int(input('Digite a velocidade do carro:'))
multa = int((velocidade - 80)*5)
if velocidade > 80:
        print(f'Você recebeu uma multa no valor de ${multa:5.2f} por ultrapassar o limite de velocidade')
if velocidade <= 80: 
        print('Velocidade está dentro do limite')