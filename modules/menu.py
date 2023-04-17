import time
from modules import message_sender
def title():
    return '''
                  $$\ $$\                               $$\                 $$\                               
      $$ |\__|                              $$ |                $$ |                              
 $$$$$$$ |$$\  $$$$$$$\  $$$$$$$\  $$$$$$\  $$$$$$$\   $$$$$$\  $$ | $$$$$$\   $$$$$$\   $$$$$$\  
$$  __$$ |$$ |$$  _____|$$  _____|$$  __$$\ $$  __$$\ $$  __$$\ $$ |$$  __$$\ $$  __$$\ $$  __$$\ 
$$ /  $$ |$$ |\$$$$$$\  $$ /      $$ /  $$ |$$ |  $$ |$$$$$$$$ |$$ |$$ /  $$ |$$$$$$$$ |$$ |  \__|
$$ |  $$ |$$ | \____$$\ $$ |      $$ |  $$ |$$ |  $$ |$$   ____|$$ |$$ |  $$ |$$   ____|$$ |      
\$$$$$$$ |$$ |$$$$$$$  |\$$$$$$$\ \$$$$$$  |$$ |  $$ |\$$$$$$$\ $$ |$$$$$$$  |\$$$$$$$\ $$ |      
 \_______|\__|\_______/  \_______| \______/ \__|  \__| \_______|\__|$$  ____/  \_______|\__|  v 1.0    
                                                                    $$ |                          
                                                                    $$ |                          
                                                                    \__|
'''
def rules():
    rules = '''
                                            
 .----.-----.-----.----.---.-.-----.
 |   _|  -__|  _  |   _|  _  |__ --|
 |__| |_____|___  |__| |___._|_____|
            |_____|
    '''

    print(rules)
    print('-' * 100)
    print('1 - Não faça flood no canal. Você SERÁ banido e eu não estou nem aí.')
    print('2 - Mantenha a janela aberta em foco, caso contrário ele vai escrever em outro lugar.')
    print('3 - Seja feliz')
    print('-' * 100)
    print()
    print()
    print()
    
def menu():
    try:
        
        print('-' * 100)
        print(title())
        print('-' * 100)
        rules()
        print('-' * 100)
        print('IMPORTANTE: Não feche o programa enquanto a rotina estiver em execução.')
        print('IMPORTANTE: Não tire de foco a janela do navegador enquanto a rotina estiver em execução.')
        print('-' * 100)
        time.sleep(5)
        print('IMPORTANTE: Digite a URL completa, incluindo o https://. Antes de executar a rotina,\nteste se ao abrir a URL ele vai focar no input de mensagem.')
        url = input('Digite a URL do canal que será utilizado:\n ')
        if not url.startswith('http'):
            raise ValueError('A URL informada é inválida.')
        print('-' * 100)
        message = input('Digite o comando que será enviado:\n ')
        print('-' * 100)
        print('IMPORTANTE: se você floodar o canal, o Discord pode te banir. O problema é seu.')
        wait_time = int(
            input('Digite o tempo de espera entre as mensagens (em segundos):\n '))
        if wait_time <= 0:
            raise ValueError('O tempo de espera deve ser maior que zero.')
        print('-' * 100)
        print('Confirme as informações abaixo: ')
        print(
            f'URL: {url}, Mensagem: {message}, Tempo de espera: {wait_time} segundos')
        choice = input('está correto? (s/n):')
        if choice.lower() == 's':
            message_sender.send_message(url, message, wait_time=wait_time)
        elif choice.lower() != 's':
            print('vamos tentar de novo então.')
            menu()
    except ValueError as ve:
        print(f"Ocorreu um erro ao executar a rotina: {str(ve)}")
        print("Encerrando programa.")
        exit()
    except Exception as e:
        print(f"Ocorreu um erro ao executar a rotina: {str(e)}")
        print("Encerrando programa.")
        exit()
