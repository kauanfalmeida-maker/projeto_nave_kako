## Definir as variáveis
combustivel = 110
tripulantes = []

## Definir funções

def viajar():
    ## Aqui vamos gatar combustível
    global combustivel ## Avisa função que vamos modificar uma variavel externa
    if(combustivel>=30):
      combustivel = combustivel - 30 
      print("A nave viajou")

    else:
       print("Você está sem combustivel suficiente. Abasteça!")

def abastecer():
    global combustivel
    combustivel = 110
    print("Tanque cheio! ⛽")

def status_nave():
    ## Mostre a quantidade de combustivel e os tripulantes
    print("\n------STATUS DA NAVE------")
    print(f"Temos {combustivel} de combustível")
    print(f"Os tripulantes são: {tripulantes}")
    print("---------------------------\n")

def registrarTripulante():
    ## Essa função pergunta o nome do tripulante e adiciona na lista de tripulantes
    novotripulante = input("Qual o nome do novo tripulante?: ") #Pergunta quem
    tripulantes.append(novotripulante) #inserimos o fulaninho
    print("Tripulante inserido com sucesso! 🚀")

## Criar um menu

while True:  ## Esse loop roda para sempre!
    print("Bem vindo ao menu interativo da nave. Por favor selecione uma opção:")
    print("\n1- Mostrar status da nave | 2- Viajar | 3-  Abastecer | 4- novo tripulante | 5- Sair")
    opcao = input("Escolha: ")
    if(opcao == "1"):
       status_nave()
    elif (opcao == "2"):
        viajar()
    elif (opcao == "3"):
        abastecer()
    elif (opcao == "4"):
        registrarTripulante()
    elif (opcao == "5"):
        print("Viagem encerrada!")
        break






# status_nave()
# registrarTripulante()
# status_nave()


# status_nave()
# viajar()
# viajar()
# status_nave()
# viajar()
# viajar()
# abastecer()
# viajar()
# status_nave()