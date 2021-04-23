from os import chdir, mkdir, path, rename, listdir, getcwd
from shutil import move
from contextlib import suppress


def cria_move(arquivo, diretorio):
    with suppress(FileExistsError):
        mkdir(diretorio)
    chdir(diretorio)
    if(path.isfile(arquivo)):
        nome, extensao = path.splitext(arquivo)
        novo_nome = nome+"_"+extensao
        novo_nome_exist = True
        while(novo_nome_exist):
            if(path.isfile(novo_nome)):
                nome, extensao = path.splitext(novo_nome)
                novo_nome = nome+"_"+extensao
            else:
                novo_nome_exist = False
        print(f"Seu arquivo {arquivo} foi renomeado para {novo_nome}")
        chdir("../")
        rename(arquivo, novo_nome)
        arquivo = novo_nome
    else:
        chdir("../")
    move(arquivo, diretorio)


def importa_arquivos():
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
    dev = ['.cpp', '.php', '.js', '.css', '.py', '.sql', '.xml', '.htm',
           '.html', '.cpp', '.java', '.c', '.dart', '.cs', '.vb', '.xhtml']

    for arquivo in listdir(path.abspath(getcwd())):
        if(path.isfile(arquivo)):
            nome, extensao = path.splitext(arquivo)
            if(arquivo != "organizer.py" or arquivo != "organizar.bat"):
                if(extensao in txt):
                    cria_move(arquivo, './txt')
                elif(extensao in word):
                    cria_move(arquivo, './word')
                elif(extensao in powerpoint):
                    cria_move(arquivo, './powerpoint')
                elif(extensao in excell):
                    cria_move(arquivo, './excell')
                elif(extensao in imagens):
                    cria_move(arquivo, './imagens')
                elif(extensao in design):
                    cria_move(arquivo, './design')
                elif(extensao in video):
                    cria_move(arquivo, './video')
                elif(extensao in audio):
                    cria_move(arquivo, './audio')
                elif(extensao in compactados):
                    cria_move(arquivo, './compactados')
                elif(extensao in pdf):
                    cria_move(arquivo, './pdf')
                elif(extensao in executaveis):
                    cria_move(arquivo, './executaveis')
                elif(extensao in dev):
                    cria_move(arquivo, './dev')
                else:
                    cria_move(arquivo, './outros')


importa_arquivos()
