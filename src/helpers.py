import locale
import os

def configure_locale(locale_str='pt_BR.UTF-8'):
    locale.setlocale(locale.LC_MONETARY, locale_str)

def format_money(value):
 
    try:
        return locale.currency(value, grouping=True)
    except ValueError:
        return value  

def encontrar_arquivo(nome_arquivo, diretorios=[]):
   
    for diretorio in diretorios:
        caminho_arquivo = os.path.join(diretorio, nome_arquivo)
        if os.path.isfile(caminho_arquivo):
            return caminho_arquivo
    return None
