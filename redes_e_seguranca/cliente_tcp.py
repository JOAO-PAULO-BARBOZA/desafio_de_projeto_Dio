'''PARA CRIAÇÃO DO CLIENTE TCP É NECESSÁRIO A IMPORTAÇÃODE ALGUMAS BIBLIOTECA BUILT-INS DO PYTHON.'''

import socket
import sys


def conexao_socket():
    try:
        conexao = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as erro:
        print('A conexão falhou!')
        print(f'Erro: {erro}')
        sys.exit()
    print('Conexão socket criada com sucessso!')


    host_alvo = input('Digite o host a ser conectado: ')
    porta_alvo = input('Digite a porta a ser conetada: ')


    try:
        conexao.connect((host_alvo, int(porta_alvo)))
        print(f'Cliente conectado com sucesso no host {host_alvo} e na porta {porta_alvo}.')
        conexao.shutdown(2) # finalização da conexão depois de 2s.

    except socket.error as erro:
        print(f'Não foi possivel se conectar ao host {host_alvo} na porta {porta_alvo}.')
        print(f'Erro: {erro}')
        sys.exit() # Necessário para sair da aplicação


if __name__ == '__main__':
    conexao_socket()
    

