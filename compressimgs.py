from tabnanny import check
import PIL
from PIL import Image
import os

import glob
import time
import sys
from progress.bar import ChargingBar, Bar

import arqfiles as log
import oslistagem  as ls


''' path = 'imagens/'
path_destino = 'imagens-resized/'

lista_de_arquivos = os.listdir(path)
print(lista_de_arquivos)
 '''
''' images = [file for file in os.listdir(path) if file.endswith(('jpeg', 'png', 'jpg'))]
for image in images:
    img = Image.open(path+image)
    img.thumbnail((800,800))
    img.save(path_destino+"resized_"+image, optimize=True, quality=80) '''


#tamanho 800 x 800 , qualidade = 80
def compress_(path, path_destino, tamanho, qualidade, newname = None):
    erros = []

    if newname is not None:
        newname = newname + '_'
    else:
        newname = ''

        max_bar = len(os.listdir(path))
        bar = Bar('Loading', fill='▋', suffix='%(percent)d%%')
        #, suffix='%(percent)d%%'
        with Bar('Comprimindo e otimizando as imagens: ', max=max_bar, fill='▋') as bar:
        

            images = [file for file in os.listdir(path) if file.endswith(('jpeg', 'png', 'jpg'))]
            for image in images:
                try:
                    img = Image.open(path+image)
                    img.thumbnail((tamanho,tamanho))
                    img.save(path_destino+newname+image, optimize=True, quality=qualidade)
                    # Do some work
                except:
                    #print(f"\nImagem com defeito: {image}")
                    img_erro = "Imagem com defeito: "+image+"\nDiretório Original: "+path+"\n"
                    erros.append(img_erro)                
                    #time.sleep(1)
                    continue
                bar.next()
            bar.finish()

    
    

#tamanho 800 x 600 , qualidade = 80
def compress2_(path, path_destino, tamanho, qualidade, newname = None):
    erros = []

    if newname is not None:
        newname = newname + '_'
    else:
        newname = ''

        max_bar = len(os.listdir(path))
        bar = Bar('Loading', fill='▋', suffix='%(percent)d%%')
        #, suffix='%(percent)d%%'
        with Bar('Comprimindo e otimizando as imagens: ', max=max_bar, fill='▋') as bar:
        

            images = [file for file in os.listdir(path) if file.endswith(('jpeg', 'png', 'jpg', 'gif', 'webp'))]
            for image in images:
                try:
                    dimensoes = tamanho.split(',')
                    tamanho1 = int(dimensoes[0])
                    tamanho2 = int(dimensoes[1])
                    img = Image.open(path+image)
                    img.thumbnail((tamanho1,tamanho2))
                    img.save(path_destino+newname+image, optimize=True, quality=qualidade)
                    # Do some work
                except:
                    #print(f"\nImagem com defeito: {image}")
                    img_erro = "Imagem com defeito: "+image+"\nDiretório Original: "+path+"\n"
                    erros.append(img_erro)                
                    #time.sleep(1)
                    continue
                bar.next()
            bar.finish()

    path_destino = path_destino.replace('/','')
    arquivo_de_log = "logs-"+path_destino+'.txt'
    log.updateArquivo(arquivo_de_log,str(erros))  

#tamanho 800 x 600 , qualidade = 80 - 
#   NAO MODIFICA O TAMANHO APENAS COMPRIMI A IMAGEM
#   13/09/2022

def compress3_(path, path_destino, tamanho, qualidade, newname = None):
    erros = []

    if newname is not None:
        newname = newname + '_'
    else:
        #newname = 'p2012-traveller-'

        print("Digite o nome dos arquivos de imagens...")
        time.sleep(0.2)

        newname = input("Nome comum da pasta de arquivos. ")
        newname = newname + '-'

        max_bar = len(os.listdir(path))
        bar = Bar('Loading', fill='▋', suffix='%(percent)d%%')
        #, suffix='%(percent)d%%'
        with Bar('Comprimindo e otimizando as imagens: ', max=max_bar, fill='▋') as bar:
        

            images = [file for file in os.listdir(path) if file.endswith(('jpeg', 'png', 'jpg', 'gif', 'webp'))]
            for image in images:
                try:
                    #dimensoes = tamanho.split(',')
                    #tamanho1 = int(dimensoes[0])
                    #tamanho2 = int(dimensoes[1])
                    img = Image.open(path+image)
                    #img.thumbnail((tamanho1,tamanho2))
                    img.save(path_destino+newname+image, optimize=True, quality=qualidade)
                    # Do some work
                except:
                    #print(f"\nImagem com defeito: {image}")
                    img_erro = "Imagem com defeito: "+image+"\nDiretório Original: "+path+"\n"
                    erros.append(img_erro)                
                    #time.sleep(1)
                    continue
                bar.next()
            bar.finish()

    path_destino = path_destino.replace('/','')
    arquivo_de_log = "logs-"+path_destino+'.txt'
    log.updateArquivo(arquivo_de_log,str(erros))  



#tamanho 800 x 600 , qualidade = 80 - 
#   NAO MODIFICA O TAMANHO APENAS COMPRIMI A IMAGEM
#   13/09/2022

def compress4_(path, path_destino, tamanho, qualidade, newname = None):
    erros = []

    if newname is not None:
        newname = newname + '_'
    else:
        #newname = 'p2012-traveller-'

        print("Digite o nome dos arquivos de imagens...")
        time.sleep(0.2)

        newname = input("Nome comum da pasta de arquivos. ")
        newname = newname + '-'

        max_bar = len(os.listdir(path))
        bar = Bar('Loading', fill='▋', suffix='%(percent)d%%')
        #, suffix='%(percent)d%%'
        with Bar('Comprimindo e otimizando as imagens: ', max=max_bar, fill='▋') as bar:
        

            images = [file for file in os.listdir(path) if file.endswith(('jpeg', 'png', 'jpg', 'gif', 'webp'))]
            for image in images:
                try:
                    dimensoes = tamanho.split(',')
                    tamanho1 = int(dimensoes[0])
                    tamanho2 = int(dimensoes[1])
                    img = Image.open(path+image)
                    img.thumbnail((tamanho1,tamanho2))
                    img.save(path_destino+newname+image, optimize=True, quality=qualidade)
                    # Do some work
                except:
                    #print(f"\nImagem com defeito: {image}")
                    img_erro = "Imagem com defeito: "+image+"\nDiretório Original: "+path+"\n"
                    erros.append(img_erro)                
                    #time.sleep(1)
                    continue
                bar.next()
            bar.finish()

    path_destino = path_destino.replace('/','')
    arquivo_de_log = "logs-"+path_destino+'.txt'
    log.updateArquivo(arquivo_de_log,str(erros)) 


#formatos_app = ['jpeg', 'png', 'jpg', 'webp']
# CONVERTE E RECORTA IMAGEM, FOI USADA PARA AS IMAGENS
# DO SCRAP comidasereceitas.com.br
def convert2_(path, path_destino, tipo, newname = None):
    erros = []

    if newname is not None:
        newname = newname + '_'
    else:
        newname = ''
        
    max_bar = len(os.listdir(path))
    bar = Bar('Loading', fill='▋', suffix='%(percent)d%%')
    #, suffix='%(percent)d%%'
    with Bar('Convertendo imagens: ', max=max_bar, fill='▋') as bar:
        #CONVERTE IMAGENS PARA WEBP
        images = [file for file in os.listdir(path) if file.endswith(('jpeg', 'png', 'jpg','gif','webp'))]
        for image in images:
            try:
                img = Image.open(path+image)
                #img.thumbnail((800,800))
                img = img.convert('RGB')
                #tira o .jpeg .jpg
                image = image.replace('.jpeg','')
                image = image.replace('.jpg','')
                image = image.replace('.png','')
                image = image.replace('.gif','')
                image = image.replace('.webp','')

                # Adicionar opção de corte nas imagens
                # corte de teste 85% = bottom = h * 0.85
                # 08/01/2022
                width, height = img.size
                left = 0
                top = 0
                right = width
                bottom = int(height * 0.85) #height
                img = img.crop((left, top, right, bottom))

                # Resizes images
                fixed_height = height
                height_percent = (fixed_height / float(img.size[1]))
                width_size = int((float(img.size[0]) * float(height_percent)))

                # modos de aliases e filtros
                #img = img.resize((width_size, fixed_height), PIL.Image.NEAREST)
                img = img.resize((width_size, fixed_height), Image.ANTIALIAS)
                #img = img.resize((width_size, fixed_height), PIL.Image.LANCZOS)               
                
                # Salva imagem
                img.save(path_destino+newname+image+'.'+tipo, tipo, optimize=True)

            except:
                img_erro = "Imagem com defeito: "+image+"\nDiretório Original: "+path+"\n"
                erros.append(img_erro)                
                #time.sleep(1)
                continue

            bar.next()
        bar.finish()

    path_destino = path_destino.replace('/','')
    arquivo_de_log = "logs-"+path_destino+'.txt'
    log.updateArquivo(arquivo_de_log,str(erros))  



#formatos_app = ['jpeg', 'png', 'jpg', 'webp']
# FUNÇÃO ORIGINAL DE CONVERSÃO
# JÁ OTIMIZADA
def convert_(path, path_destino, tipo, newname = None):
    erros = []

    if newname is not None:
        newname = newname + '_'
    else:
        newname = ''
        
    max_bar = len(os.listdir(path))
    bar = Bar('Loading', fill='▋', suffix='%(percent)d%%')
    #, suffix='%(percent)d%%'
    with Bar('Convertendo imagens: ', max=max_bar, fill='▋') as bar:
        #CONVERTE IMAGENS PARA WEBP
        images = [file for file in os.listdir(path) if file.endswith(('jpeg', 'png', 'jpg','gif','webp'))]
        for image in images:
            try:
                img = Image.open(path+image)
                #img.thumbnail((800,800))
                img = img.convert('RGB')
                #tira o .jpeg .jpg
                image = image.replace('.jpeg','')
                image = image.replace('.jpg','')
                image = image.replace('.png','')
                image = image.replace('.gif','')
                image = image.replace('.webp','')

                # Salva imagem
                img.save(path_destino+newname+image+'.'+tipo, tipo, optimize=True)

            except:
                img_erro = "Imagem com defeito: "+image+"\nDiretório Original: "+path+"\n"
                erros.append(img_erro)                
                #time.sleep(1)
                continue

            bar.next()
        bar.finish()

    path_destino = path_destino.replace('/','')
    arquivo_de_log = "logs-"+path_destino+'.txt'
    log.updateArquivo(arquivo_de_log,str(erros))  



# Check if has transparency
def has_transparency(file):
    image = Image.open(file).convert('RGBA') 
    alpha_range = image.getextrema()[-1]

    if alpha_range == (255,255):
        #print(f"{file}: is not transparent")
        return False
    else:
        return True
        #print(f"{file}: transparent")


# Criada em 19/01/2022
# Função que converte imagens para outro formato
# porém mantem a transparencia
def convert_transparent(path, myimage, extensao, path_destino):
    img = Image.open(path+myimage)
    pixdata = img.load()
    img = img.convert("RGBA")
    width, height = img.size
    for y in range(height):
        for x in range(width):
            if pixdata[x, y] == (255, 255, 255, 255):
                pixdata[x, y] = (255, 255, 255, 0)

    myimage = myimage.replace('.png','')
    myimage = myimage.replace('.jpg','')
    myimage = myimage.replace('.jpeg','')
    myimage = myimage.replace('.gif','')
    myimage = myimage.replace('.webp','')
    

    # Salva imagem
    img.save(path_destino+myimage+'.'+extensao, extensao, optimize=True)
    

#formatos_app = ['jpeg', 'png', 'jpg', 'webp']
# Semelhante a função anterior (original)
# Com a verificação de transparencia ou alpha na imagem
# e salvamento da nova imagem convertida de acordo com RGB ou RGBA
# FUNÇÃO de CONVERSÃO COM TRANSPARENCIA # RGBA usa as 2 funções acima
def convert_rgba_(path, path_destino, tipo, newname = None):
    erros = []
    if newname is not None:
        newname = newname + '_'
    else:
        newname = ''        
    max_bar = len(os.listdir(path))
    bar = Bar('Loading', fill='▋', suffix='%(percent)d%%')
    #, suffix='%(percent)d%%'
    with Bar('Convertendo imagens: ', max=max_bar, fill='▋') as bar:
        #CONVERTE IMAGENS PARA WEBP
        images = [file for file in os.listdir(path) if file.endswith(('jpeg', 'png', 'jpg','gif','webp'))]
        for image in images:
            try:
                #print(path+image)
                # VERIFICA SE NA IMAGEM EXISTE TRASPARÊNCIA                
                if has_transparency(path+image) is True:
                    # Converte imagens com transparência                    
                    convert_transparent(path, image, tipo, path_destino)                
                else:
                    # CONVERTE IMAGENS SEM TRANSPARENCIA
                    img = Image.open(path+image)
                    #img.thumbnail((800,800))
                    img = img.convert('RGB')
                    #tira o .jpeg .jpg
                    image = image.replace('.webp','')
                    image = image.replace('.jpeg','')
                    image = image.replace('.jpg','')
                    image = image.replace('.png','')
                    image = image.replace('.gif','')
                    # Salva imagem
                    img.save(path_destino+newname+image+'.'+tipo, tipo, optimize=True)

            except:
                img_erro = "Imagem com defeito: "+image+"\nDiretório Original: "+path+"\n"
                erros.append(img_erro)                
                #time.sleep(1)
                continue

            bar.next()
        bar.finish()

    path_destino = path_destino.replace('/','')
    arquivo_de_log = "logs-"+path_destino+'.txt'
    log.updateArquivo(arquivo_de_log,str(erros))  



# NOVA Adicionada 08/01/2022
def func_converter_imagens(path_origem,path_destino, tamanho_anterior):    
        clear = lambda: os.system('cls')
        
        clear()
        print("Digite as opções de conversão da imagens.")
        time.sleep(0.2)

        clear = lambda: os.system('cls')
        clear()
        
        print("Digite as opções de conversão da imagens..")
        time.sleep(0.2)

        while True:
            clear = lambda: os.system('cls')
            clear()
            
            print("(0) Voltar ")
            formatos_app = ['jpeg', 'png', 'jpg', 'webp']
            y = 1
            for tipos in formatos_app:
                print(f"({y}) {tipos}")
                y+=1
                
            try:
                format_imagem = int(input("Digite o formato da imagems para converter: "))
                if(format_imagem == 0):
                    return 1
                if(format_imagem >= 1 and format_imagem <= 4):

                    tipo = formatos_app[format_imagem-1]
                    print(f"\nPasta Origem {path_origem}")
                    print(f"Pasta Destino {path_destino}")
                    print(f"Formato a ser convertido {tipo}")
                    time.sleep(1)
                    pausar = input("\nTudo pronto, deseja executar\nA conversão de FORMATO em massa das imagens\n Neste diretório? (y/n) ")
                    if pausar == 'n':
                        sys.exit()
                    else:
                        # pega o tempo inicial do upload
                        upload_time = time.time()
                        
                        # Faz a conversão das imagens após as escolhas
                        # convert_ (FUNÇÃO ORIGINAL)
                        # convert2_ (FUNÇÃO COM RECORTE)
                        # * -> convert_rgba_ (FUNÇÃO QUE CONVERTE IMAGENS COM TRANSPARENCIA)
                        # ADICIONADA A VERIFICACAO DE TRANSPARENCIA NA IMAGEM
                        convert_rgba_(path_origem, path_destino, tipo)

                        tempo = (time.time() - upload_time)

                        if tempo < 60:
                            segundos = time.time() - upload_time
                            segundos = ("%.2f" % segundos)
                            timeDuration = "- convert in %s seconds -" % (segundos)
                        else:
                            tminutos = (time.time() - upload_time)
                            tminutos = tminutos / 60

                            tminutos = ("%.2f" % tminutos)
                            timeDuration = "- convert in %s minutos -" % str(tminutos)                                                    
                            
                    size_pasta_comprimida, size_gigas_new = ls.get_folder_sizes(path_destino)
                    tamanho_resultado = float(tamanho_anterior) - float(size_gigas_new)

                    if float(tamanho_anterior) < 1:
                        tamanho_certo = str(float(tamanho_anterior) * 1024) + ' MB'
                    else:
                        tamanho_certo = str(tamanho_anterior) + ' GB'
                    
                    if float(tamanho_resultado) < 1:
                        tresultado = str(("%.2f" % (float(tamanho_resultado) * 1024))) + ' MB'
                    else:
                        tresultado = str("%.2f" % float(tamanho_resultado)) + ' GB'
                        
                    
                    print(f"Resultado: \nTamanho antes: {tamanho_certo} - Depois: {size_pasta_comprimida}")
                    print(f"Economia de {tresultado}")
                    print(f"\nConversão das imagens concluída com sucesso.\nO resultado está na pasta: {path_destino}")
                    print(timeDuration)
                    print("Digite (y) Para abrir a pasta com as imagens convertidas... ou")
                    pausar = input("\nPressione uma tecla.. para continuar! ")
                    if(pausar == 'y'):

                        simp_path = './'+path_destino.replace('/','')

                        abs_path = os.path.abspath(simp_path)

                        path = os.path.realpath(abs_path)
                        os.startfile(path)
                        
                    return 1
            

            except ValueError:
                print('\nOpção tem que ser um valor inteiro')
                time.sleep(1)  


def erase_all_(path_destino, string_matches):
    i = 0
    for file in os.listdir(path_destino):
        if any(x in file for x in string_matches):
            os.remove(path_destino+file)
            i+=1
    return i



def openimg_(path_destino, nome_da_imagem):
    image = Image.open(path_destino+nome_da_imagem)
    image.show()


def func_comprimir_imagens(path_origem,path_destino,tamanho_anterior):
    
    while True:
        try:
            clear = lambda: os.system('cls')
            clear()
            print("Digite as opções de compressão da imagens.")
            time.sleep(0.3)

            clear = lambda: os.system('cls')
            clear()
            
            print("Digite as opções de compressão da imagens..")
            time.sleep(0.2)

            clear = lambda: os.system('cls')
            clear()

            print("Digite as opções de compressão da imagens...")
            time.sleep(0.2)

            #dimensoes = input("Digite o largura,altura para dimensão padrão. Ex: 800,600 (em pixels) ")
            dimensoes = "1920,1280"
            
            #qualidade = int(input("Digite a qualidade desejada. Ex: 0 a 100 (%) "))
            qualidade = 80

            print(f"\nPasta Origem {path_origem}")
            print(f"Pasta Destino {path_destino}")
            print(f"Dimensoes {dimensoes} x {dimensoes} px")
            print(f"Qualidade: {qualidade} %")
          
            time.sleep(1)
            pausar = input("\nTudo pronto, deseja executar\nA compressão em massa das imagens\nNeste diretório? (y/n) ")
            if pausar == 'n':
                sys.exit()
            else:
                # pega o tempo inicial do upload
                upload_time = time.time()
                compress4_(path_origem,path_destino,dimensoes,qualidade)
                                
                tempo = (time.time() - upload_time)

                if tempo < 60:
                    segundos = time.time() - upload_time
                    segundos = ("%.2f" % segundos)
                    timeDuration = "- compress in %s seconds -" % (segundos)
                else:
                    tminutos = (time.time() - upload_time)
                    tminutos = tminutos / 60

                    tminutos = ("%.2f" % tminutos)
                    timeDuration = "- compress in %s minutos -" % str(tminutos)

            size_pasta_comprimida, size_gigas_new = ls.get_folder_sizes(path_destino)
            tamanho_resultado = float(tamanho_anterior) - float(size_gigas_new)

            if float(tamanho_anterior) < 1:
                tamanho_certo = str(float(tamanho_anterior) * 1024) + ' MB'
            else:
                tamanho_certo = str(tamanho_anterior) + ' GB'
            
            if float(tamanho_resultado) < 1:
                tresultado = str(("%.2f" % (float(tamanho_resultado) * 1024))) + ' MB'
            else:
                tresultado = str("%.2f" % float(tamanho_resultado)) + ' GB'
                
            
            print(f"Resultado: \nTamanho antes: {tamanho_certo} - Depois: {size_pasta_comprimida}")
            print(f"Economia de {tresultado}")
            print(f"Compressão das imagens concluída com sucesso.\nO resultado está na pasta: {path_destino}")
            print(timeDuration)
            print("Digiter (y) Para abrir a pasta com as imagens comprimidas... ou")
            pausar = input("\nPressione uma tecla.. para continuar! ")
            if(pausar == 'y'):

                simp_path = './'+path_destino.replace('/','')

                abs_path = os.path.abspath(simp_path)

                path = os.path.realpath(abs_path)
                os.startfile(path)
                
            return 1

        except ValueError:
            print('\nOpção tem que ser um valor inteiro')
            time.sleep(1)
            
        #imgs.compress_(path_origem,path_destino,800,80)