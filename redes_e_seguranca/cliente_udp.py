import socket 

conexao = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
'''Assim como no tcp aqui também né necessario a criação de um objeto de conexão, que no caso é o "conexao".'''

print('cliente criado com sucesso!')

host = 'localhost'
porta = 5433
menssagem = 'Hi server, this is a test message, are you there?'


try:
    
    print(f'Cliente: {menssagem}')
    conexao.sendto(menssagem.encode(), (host, 5432))

    dados, servidor = conexao.recvfrom(4096)
    dados = dados.decode()
    print(f'Cliente: {dados}')

finally:
    print('Cliente: fechando a conexão!')
    conexao.close()
