from back import *
print(f"""{colorama.Fore.GREEN}	
	----------------------------
	|GET YOUR OWN WHATSAPP LINK|
	----------------------------
""")

try:
    phone = int(input('DIGITE O SEU NÚMERO:'))
    message = str(input('DIGITE SUA MENSAGEM AQUI:'))
    generate_link(message, phone)
except:
    print(f'\n{colorama.Fore.RED}ACONTEU UM ERRO NÃO PROGRAMÁVEL! TENTE NOVAMENTE')
print(f'\n{colorama.Fore.YELLOW}By: SÍLVIO SILVA') 