import time
import sys
import os
import fdiretorio as fd

def escolhe_path_origem():  

    while True:
        clear = lambda: os.system('cls')
        clear()

        path_data = 'data'
        pastas_path_data = os.listdir(path_data)
        i = 1
        print("Escolha qual pasta:\n")
        print("\nDigite (0) Para Voltar!\n")
        for pasta in pastas_path_data:            
            print("Digite ("+str(i)+") para escolher a pasta: "+pasta)
            i+=1      

        try: 
            print('\n')
            opcao = int(input("------- Digite uma opção: ------- "))
            
            # VOLTAR TELA INICIAL
            if(opcao == 0):
                return('inicio')
                
            
            if(opcao >= 1 and opcao <= len(pastas_path_data) ):
                pasta_origem = 'data/'+pastas_path_data[opcao-1]
                dir_padrao = os.listdir(pasta_origem)
                if len(dir_padrao) == 0:
                  
                    abs_path = os.path.abspath(pasta_origem)                
                    print(f"\nNão Existem Imagens nesta pasta ainda.\nPor favor coloque alguns arquivos.")
                    time.sleep(1)
                    pausar = input("\nDeseja abrir a Pasta Criada?\n\nPressione (y) para abrir.\nou\nPressione uma tecla.. para continuar! ")
                    if pausar == 'y':
                        os.startfile(abs_path)
                        #return 0
                
                    #senao tiver imagens voltar para inicio
                    return('inicio')
                    #inicio()

                else:
                    
                    abs_path = os.path.abspath(pasta_origem)
                    return(abs_path)   
               

            else:
                print("\n------- Opção não existe! -------")
                time.sleep(1)                
                continue

        except ValueError:
            print('\n- Opção tem que ser um valor inteiro -')
            time.sleep(1)
           



def cria_path_origem():
    clear = lambda: os.system('cls')
    clear()         
    
    nome_diretorio = input("\nDigite o nome da pasta: ")
    print(f"\nCriando a pasta {nome_diretorio}")
    time.sleep(1)
    try:
        fd.CriaDiretorio('./data/'+nome_diretorio)
        path_origem = 'data/'+nome_diretorio
        dir_padrao = os.listdir(path_origem)
        if len(dir_padrao) == 0:
            #cria o path de origem padrao
            simp_path = 'data/'+nome_diretorio
            abs_path = os.path.abspath(simp_path)
            print(f"Pasta de Origem Criada!\n\nCaminho da Pasta:\n{abs_path}")
            time.sleep(1)
            print(f"\nNão Existem Imagens nesta pasta ainda.\nPor favor coloque alguns arquivos.")
            time.sleep(1)
            pausar = input("\nDeseja abrir a Pasta Criada?\n\nPressione (y) para abrir.\nou\nPressione uma tecla.. para continuar! ")
            if pausar == 'y':
                os.startfile(abs_path)
                #return 0
                
            #senao tiver imagens voltar para inicio
            return('inicio')
            #inicio()

        else:
            simp_path = 'data/'+nome_diretorio
            abs_path = os.path.abspath(simp_path)
            return(abs_path)

        
    except:
        print("Ops algo deu errado")
        time.sleep(1)



        

def path_origem_default():
    clear = lambda: os.system('cls')
    clear()
    
    path_origem = 'data/default'
    dir_padrao = os.listdir(path_origem)
    if len(dir_padrao) == 0:
        #cria o path de origem padrao
        simp_path = 'data/default'
        abs_path = os.path.abspath(simp_path)
        print(f"\nNão Existem Imagens nesta pasta ainda.\nPor favor coloque alguns arquivos.\n\nCaminho da Pasta Padrão é:\n{abs_path}")
        time.sleep(1)
        pausar = input("\nDeseja abrir a Pasta de Origem Padrao?\n\nPressione (y) para abrir.\nou\nPressione uma tecla.. para continuar! ")
        if pausar == 'y':
            os.startfile(abs_path)                    
        
        #senao tiver imagens voltar para inicio
        return('inicio')
        #inicio()                        

    else:
        simp_path = 'data/default'
        abs_path = os.path.abspath(simp_path)
        print(f"\nPath Origem: {abs_path}")
        return abs_path



def principal_open():

    clear = lambda: os.system('cls')
    clear()

    while True:
        i = 1
        print("MANAGER IMAGES\n\n")

        print("Digite (0) Para Sair!\n")
        print("Digite (1) Escolher Pasta de Origem")        
        print("Digite (2) Criar uma Pasta de Origem")
        print("Digite (3) Usar Pasta de Origem Padrão")
        
                
        try: 
            print('\n')
            opcao = int(input("------- Digite uma opção: ------- "))
            
            # SAIR DO APP
            if(opcao == 0):
                print("\nBye..")
                time.sleep(1)
                sys.exit()
          
            elif (opcao == 1):
                abs_path = escolhe_path_origem()
                if abs_path == 'inicio':
                    principal_open()
                else:
                    #print(abs_path)
                    return(abs_path)
            
            elif (opcao == 2):
                abs_path = cria_path_origem()
                if abs_path == 'inicio':
                    principal_open()
                
                else:
                    #print(abs_path)
                    return abs_path

            elif (opcao == 3):
                abs_path = path_origem_default()
                if abs_path == 'inicio':
                    principal_open()
                
                else:
                    #print(abs_path)
                    return abs_path
                    
                    
            else:
                print("\n------- Opção não existe! -------")
                time.sleep(1)
                clear = lambda: os.system('cls')
                clear()
                continue

        except ValueError:
            print('\n- Opção tem que ser um valor inteiro -')
            time.sleep(1)
            clear = lambda: os.system('cls')
            clear()


