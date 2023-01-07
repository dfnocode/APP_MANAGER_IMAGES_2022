# FUNCAO QUE CRIA O DIRETORIO DA PAGINA PARA SALVAR OS ARQUIVOS DAS
# por PAGINA
#
def CriaDiretorio(path_dir):    
    import os
    #dirTemp = './temp'
    dirTemp = path_dir
    
    try:
        os.mkdir(dirTemp)
    except OSError:
        os.rmdir(dirTemp)
        os.mkdir(dirTemp)