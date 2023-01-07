import re
import os
import compressimgs as cpx
import sys
import time
import datetime
import fdiretorio as vai
import menuapp as menu

import openjanelinha as janela


def inicio():         

    while True:
            
        clear = lambda: os.system('cls')
        clear()

        # pega o tempo inicial do upload
        upload_time = time.time()

        #path_destino = 'teste-compress/'

        #simp_path = '../SUPERSCRAPER/cozinhas/mexican recipes/images'
        #simp_path = '../SUPERSCRAPER/cozinhas/teste/images'
        abs_path = menu.principal_open()
        

        #print(abs_path)

        #print('fechou')
        #sys.exit()
        
        #time.sleep(1)
        #path_destino = nome_diretorio+'/'

        #simp_path = '../SUPERSCRAPER/cozinhas/'+ pasta_receita +'/images'

        #path_origem_teste = os.path.abspath(simp_path)
        #path_origem_teste = path_origem_teste + '/'
        #print(path_origem_teste)
        
        #simp_path = '../SUPERSCRAPER/cozinhas/mexican recipes/images'

        #pega o path absoluto da pasta de imagens
        #abs_path = os.path.abspath(simp_path)


        # CRIA O PATH DE ORIGEM NO CASO
        # APENAS O PRIMEIRO DIRETORIO
        # MEXICAN RECIPES 
        # SERA IMPLEMENTANDO 
        # INICIALMENTE
        path_origem = abs_path + '\\'

        print(abs_path)

        arr = os.listdir(path_origem)

        total_size = 0

        for imgs in arr:
            file_size = os.path.getsize(path_origem+imgs)
            total_size += file_size

            #print("File Size is :", file_size, "bytes")
            #break

        size_in_gigabytes = total_size/(1024*1024*1024)
        total_size = ("%.2f" % size_in_gigabytes)
        total_de_arquivos = len(arr)

        # PROCURA AS IMAGENS DA RECEITA PELO ID DELA REGISTRADO NO BANCO DE DADOS
        # RETORNA UMA LISTA

        #imagens_da_receita, cont = lista_imagens_da_receita(6468,abs_path)
        #print(imagens_da_receita)
        #print('Total de Imagens: '+str(cont))

        tempo = (time.time() - upload_time)

        if tempo < 60:
            segundos = time.time() - upload_time
            segundos = ("%.2f" % segundos)
            timeDuration = "- load in %s seconds -" % (segundos)
        else:
            tminutos = (time.time() - upload_time)
            tminutos = tminutos / 60

            tminutos = ("%.2f" % tminutos)
            timeDuration = "- load in %s minutos -" % str(tminutos)


        clear = lambda: os.system('cls')
        clear()    
        print(f"Pasta Origem: {path_origem}")    
        print(f"\nTotal de Arquivos: {len(arr)}")
        print(f"Tamanho total: {total_size} GB")
        print(timeDuration)   

        try:
            menu1 = input('\nDeseja executar o gerenciador de imagens? (y/n) ou (v) Voltar ')       
            
            if(menu1 == 'v'):
                inicio()
            elif(menu1=='y'):
                break
            elif (menu1=='n'):
                sys.exit()
            else:
                print('\nOpção inexistente')
                time.sleep(1)    

        
        except ValueError:
            print('\nOpção inexistente')
            time.sleep(1)    
   

    while True:

        clear = lambda: os.system('cls')
        clear()
        print(f"Pasta Origem: {path_origem}")
        print(f"\nTotal de Arquivos: {len(arr)}")
        print(f"Tamanho total: {total_size} GB")
        print(timeDuration)  
        print("\nTchunai Images Manager\n")
        print("Menu: (1) Comprimir  (2) Converter (0) Sair")
        
        try:
            num = int(input('Digite uma opção: '))

            #OPCAO COMPRIMIR
            if num == 1:
                print('\nComprimir')
                time.sleep(1)

                option1 = input("Deseja criar um diretorio? (y,n) ")
                if option1 == 'y':
                    nome_diretorio = input("Digite o nome da pasta: ")
                    print(f"Criando a pasta {nome_diretorio}")
                    time.sleep(1)
                    try:
                        vai.CriaDiretorio('./'+nome_diretorio)
                        print("Diretorio criado com sucesso")
                        time.sleep(1)
                        
                    except:
                        print("Ops algo deu errado")
                        time.sleep(1)
                        continue
                    
                    time.sleep(1)
                    path_destino = nome_diretorio+'/'
                    
                    r_compressao = cpx.func_comprimir_imagens(path_origem,path_destino,total_size)
                    if r_compressao == 1:
                        inicio()
                
                    
                elif option1 == 'n':
                    
                    #cria um diretorio padrao
                    try:
                        vai.CriaDiretorio('./imgs_convertidas')
                        print("Criando diretorio padrao /imgs_convertidas")
                        time.sleep(1)
                        

                    except:
                        print("Ops algo deu errado")
                        time.sleep(1)
                        continue

                    path_destino = 'imgs_convertidas/'
                    r_compressao = cpx.func_comprimir_imagens(path_origem,path_destino)
                    if r_compressao == 1:
                        inicio()

                    #print("Digite as opções de compressão da imagens")
                    time.sleep(1)
                else:
                    print("\nO sistema criará uma pasta padrao para as imagens apos a compressao /imgs_convertidas\n\nReiniciando programa.")

                    time.sleep(3)
                    continue

                                
                

            #OPCAO CONVERTER        
            elif num == 2:
                print('\nConverter')
                time.sleep(1)
                option2 = input("Deseja criar um diretorio? (y,n) ")
                if option2 == 'y':
                    nome_diretorio = input("Digite o nome da pasta: ")
                    print(f"Criando a pasta {nome_diretorio}")
                    time.sleep(1)
                    try:
                        vai.CriaDiretorio('./'+nome_diretorio)
                        print("Diretorio criado com sucesso")
                        time.sleep(1)
                        
                    except:
                        print("Ops algo deu errado")
                        time.sleep(1)
                        continue
                    
                    time.sleep(1)
                    path_destino = nome_diretorio+'/'
                    
                    r_conversao = cpx.func_converter_imagens(path_origem,path_destino,total_de_arquivos)
                    if r_conversao == 1:
                        inicio()
                
                    
                elif option2 == 'n':
                    
                    #cria um diretorio padrao
                    try:
                        vai.CriaDiretorio('./imgs_convertidas')
                        print("Criando diretorio padrao /imgs_convertidas")
                        time.sleep(1)
                        

                    except:
                        print("Ops algo deu errado")
                        time.sleep(1)
                        continue

                    path_destino = 'imgs_convertidas/'
                    r_conversao = cpx.func_converter_imagens(path_origem,path_destino,total_de_arquivos)
                    if r_conversao == 1:
                        inicio()

                    #print("Digite as opções de compressão da imagens")
                    time.sleep(1)
                else:
                    print("\nO sistema criará uma pasta padrao para as imagens apos a compressao /imgs_convertidas\n\nReiniciando programa.")

                    time.sleep(3)
                    continue
               
               
            elif num == 0:
                break
            else:
                continue

        except ValueError:
            print('\nOpção Inexistente')
            time.sleep(1)
    
       
retorno = inicio()


#imgs.compress_(path_origem,path_destino,800,80)

#imgs.convert_(path_origem,path_destino,'webp','tesao_')

#imgs.openimg_('imagens/','1010_enchiladas-new-mexico-style_F4544457.jpg')

#apaga arquivos de acordo com as string de sugestao na lista 
# abaixo e retorna o numero de arquivo apagados
''' string_matches = ['resized', 'converting', '6491']
apagadas = imgs.erase_all_(path_destino, string_matches)
print(f"Total de imagens apagadas: {apagadas}")
 '''
 








