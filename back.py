import colorama
import os, platform
colorama.init(autoreset=True) #Iniciando o Colorama
if 'windows' in platform.system().lower():
    cmd = 'cls'
else:
    cmd = 'clear'
os.system(cmd)
filename = 'yourLink.txt'
def create_file(filename):
    if os.path.isfile(filename):
        print(f'Encontre o seu link no ficheiro de texto {filename}') 
    else:
        file = open(filename,'w+')
        print(f'Encontre o seu link no ficheiro de texto {filename}')
create_file(filename)
def generate_link(message, phone: int):
    try:
        if len(message) <= 0:
            print(f'{colorama.Fore.RED}ESCREVA ALGUMA COISA PARA A MENSAGEM')
        else:
            text = message.replace(' ', '%')
            link = f'api.whatsapp.com/send?phone={phone}&text={text}'
            w_link = open(filename,'w') 
            w_link.write(link)
            w_link.close()
            print(f'\n{colorama.Fore.GREEN}[!]SUCESSO! O SEU LINK FOI CRIADO')
    except:
        print(f'{colorama.Fore.RED}ACONTEU UM ERRO NÃO PROGRAMÁVEL! TENTE NOVAMENTE.')
