import time
import sys
import os

def principal_open():

    clear = lambda: os.system('cls')
    clear()

    while True:
        i = 1
        print("MANAGER IMAGES\n\n")

        print("(0) Para Sair!\n")
        print("Digite (1) Escolher Pasta de Origem")
        print("Digite (2) Usar Pasta de Origem Padrão")
        
                
        try: 
            print('\n')
            opcao = int(input("------------------ Digite uma opção: "))
            
            # SAIR DO APP
            if(opcao == 0):
                sys.exit()
          
            elif (opcao == 1):
                configuracao = 'config_pasta_origem'
                return configuracao
            
            elif (opcao == 2):
                configuracao = 'pasta_origem_padrao'
                return configuracao

            else:
                print("Opção não existe!")
                time.sleep(1)
                clear = lambda: os.system('cls')
                clear()
                continue

        except ValueError:
            print('\nOpção tem que ser um valor inteiro')
            time.sleep(1)
            clear = lambda: os.system('cls')
            clear()




def set_path_cozinha():
    opcoes = ['mexican recipes', 'italian recipes','chinese recipes', 'indian recipes','thai recipes', 'asian recipes', 'latin american recipes', 'middle eastern recipes', 'african recipes', 'european recipes', 'australian and new zealander recipes', 'canadian recipes', 'french recipes', 'japanese recipes', 'korean recipes', 'mediterranean diet', 'u.s. recipes']
  
    clear = lambda: os.system('cls')
    clear()
   
    while True:
        i = 1
        print("MANAGER IMAGES\n\n")
        print("Digite (99) Escolher Pasta de Origem\n")
        print("Digite (98) Pasta Teste de Origem\n")
        print("(0) Para Sair!\n")
        for cozinha in opcoes:
        
           print(f"({i}) {cozinha}")
           i+=1

        try: 
            pasta = int(input("------------------ Digite uma opção: "))
            if(pasta == 0):
                sys.exit()
            if(pasta >= 1 and pasta <= 17 ):
                cozinha_escolhida = opcoes[pasta-1]
                return cozinha_escolhida                

            elif (pasta == 99):
                cozinha_escolhida = 'config_pasta_origem'
                return cozinha_escolhida
            
            elif (pasta == 98):
                cozinha_escolhida = 'teste'
                return cozinha_escolhida

            else:
                print("Opção não existe!")
                time.sleep(1)
                clear = lambda: os.system('cls')
                clear()
                continue

        except ValueError:
            print('\nOpção tem que ser um valor inteiro')
            time.sleep(1)
            clear = lambda: os.system('cls')
            clear()




''' print(set_path_cozinha()) '''