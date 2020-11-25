import os
import shutil

def criaMove(arquivo, diretorio):
    if os.path.isdir(diretorio):
        pass
    else:
        os.mkdir(diretorio)
    os.chdir(diretorio)
    if(os.path.isfile(arquivo)):
        nome, extensao = os.path.splitext(arquivo)
        novo_nome = nome + "_"+extensao
        if(os.path.isfile(novo_nome)):
            nome, extensao = os.path.splitext(novo_nome)
            novo_nome = nome + "_"+extensao
            if(os.path.isfile(novo_nome)):
                nome, extensao = os.path.splitext(novo_nome)
                novo_nome = nome + "_"+extensao
                if(os.path.isfile(novo_nome)):    
                    nome, extensao = os.path.splitext(novo_nome)
                    novo_nome = nome + "_"+extensao
                    if(os.path.isfile(novo_nome)):
                        nome, extensao = os.path.splitext(novo_nome)
                        novo_nome = nome + "_"+extensao
                        if(os.path.isfile(novo_nome)):
                            nome, extensao = os.path.splitext(novo_nome)
                            novo_nome = nome + "_"+extensao
                            if(os.path.isfile(novo_nome)):    
                                nome, extensao = os.path.splitext(novo_nome)
                                novo_nome = nome + "_"+extensao
        print(f'Seu arquivo {arquivo} foi renomeado {novo_nome}')
        os.chdir('../')
        os.rename(arquivo, novo_nome)
        shutil.move(novo_nome, diretorio)
    else:
        shutil.move(arquivo, diretorio)

def importaArquivos():
    txt = ['.txt']
    word = ['.docx', '.doc', '.rtf', '.odt']
    powerpoint = ['.pptx', '.ppt']
    excell = ['.xlsx', '.xls', '.csv']
    imagens = ['.bmp', '.rle', '.dib', '.gif', '.jpg', '.jpeg', '.jpe', '.png']
    design = ['.psd', '.edf', '.cdr', '.ai']
    video = ['.flv', '.mp4', '.mov', '.mkv', '.avi', '.mpeg', '.rmvb']
    audio = ['.mp3', '.wma', '.aac', '.ogg', '.ac3', '.wav']
    compactados = ['.zip', '.rar', '.7z']
    pdf = ['.pdf']
    executaveis = ['.exe', '.msi']
    html = ['.htm', '.html']
    bd = ['.sql', '.xml']
    python = ['.py']
    css = ['.css']
    javaScript = ['.js']
    php = ['.php']


    # for arquivos  in os.walk(os.listdir(os.getcwd())):
    for arquivos  in os.listdir(os.path.abspath(os.getcwd())):
        if(os.path.isfile(arquivos)):
            nome, extensao = os.path.splitext(arquivos)
            if(arquivos!="organizer.py"):
                if(extensao in txt):
                    criaMove(arquivos, './txt')
                elif(extensao in word):
                    criaMove(arquivos, './word')
                elif(extensao in powerpoint):
                    criaMove(arquivos, './powerpoint')   
                elif(extensao in excell):
                    criaMove(arquivos, './excell')
                elif(extensao in imagens):
                    criaMove(arquivos, './imagens')
                elif(extensao in design):
                    criaMove(arquivos, './design')
                elif(extensao in video):
                    criaMove(arquivos, './video')
                elif(extensao in audio):
                    criaMove(arquivos, './audio')
                elif(extensao in compactados):
                    criaMove(arquivos, './compactados')
                elif(extensao in pdf):
                    criaMove(arquivos, './pdf')
                elif(extensao in executaveis):
                    criaMove(arquivos, './executaveis')
                elif(extensao in html):
                    criaMove(arquivos, './html')
                elif(extensao in bd):
                    criaMove(arquivos, './bd')
                elif(extensao in python):
                    criaMove(arquivos, './python')
                elif(extensao in css):
                    criaMove(arquivos, './css')
                elif(extensao in javaScript):
                    criaMove(arquivos, './javaScript')
                elif(extensao in php):
                    criaMove(arquivos, './php')
                else:
                    criaMove(arquivos, './outros')
importaArquivos()