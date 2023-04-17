import time

def wait(wait_time):
    start_time = time.monotonic()
    print(f'Próxima execução em {wait_time // 60} minutos e {wait_time % 60} segundos.')
    while time.monotonic() - start_time < wait_time:
        remaining_time = int(wait_time - (time.monotonic() - start_time))
        print(f'Restante: {remaining_time // 60} minutos e {remaining_time % 60} segundos.', end='\r')
        time.sleep(1)
    print('Tempo de espera encerrado.')
