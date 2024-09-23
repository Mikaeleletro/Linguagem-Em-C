#Entrada permitida / não permitida
nome = (str(input("Qual seu Nome? ")))
idade = (int(input("Qual sua idade? ")))
if idade>=18:
  print (f"Olá {nome}, Pode Passar")
else:
  print (f"Olá {nome}, Não pode passar")