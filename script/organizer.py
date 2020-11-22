import os
import shutil

def criaMove(arquivo, diretorio):
    if os.path.isdir(diretorio):
        pass
    else:
        os.mkdir(diretorio)
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

    for pastaAtual, subPastas, arquivos  in os.walk(os.path.abspath(os.getcwd())):
        for arquivo in arquivos:
            nome, extensao = os.path.splitext(arquivo)
            if(nome!='organizer' or nome!='organizar'):
                if(extensao in txt):
                    criaMove(arquivo, './txt')
                elif(extensao in word):
                    criaMove(arquivo, './word')
                elif(extensao in powerpoint):
                    criaMove(arquivo, './powerpoint')   
                elif(extensao in excell):
                    criaMove(arquivo, './excell')
                elif(extensao in imagens):
                    criaMove(arquivo, './imagens')
                elif(extensao in design):
                    criaMove(arquivo, './design')
                elif(extensao in video):
                    criaMove(arquivo, './video')
                elif(extensao in audio):
                    criaMove(arquivo, './audio')
                elif(extensao in compactados):
                    criaMove(arquivo, './compactados')
                elif(extensao in pdf):
                    criaMove(arquivo, './pdf')
                elif(extensao in executaveis):
                    criaMove(arquivo, './executaveis')
                elif(extensao in html):
                    criaMove(arquivo, './html')
                elif(extensao in bd):
                    criaMove(arquivo, './bd')
                elif(extensao in python):
                    criaMove(arquivo, './python')
                elif(extensao in css):
                    criaMove(arquivo, './css')
                elif(extensao in javaScript):
                    criaMove(arquivo, './javaScript')
                elif(extensao in php):
                    criaMove(arquivo, './php')
                else:
                    criaMove(arquivo, './outros')
importaArquivos()