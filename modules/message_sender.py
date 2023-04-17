from .browser import open_browser, type_message, close_browser
from .timer import wait

def send_message(url, message, wait_time=None):
    open_browser(url)
    type_message(message)
    print('Mensagem enviada com sucesso!')
    print('O comando executado foi: ' + message)
    close_browser()

    if wait_time is not None:
        wait(wait_time)

    send_message(url, message, wait_time=wait_time)
