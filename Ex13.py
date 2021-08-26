largura = float(input("Digite a largura de sua parede:"))
altura = float(input("Digite a altura de sua parede: "))

novo = float((largura*altura)/2)
media = float(novo/4)

print ("Precisa-se de {} litros de tinta para pintar essa parede.".format(media))