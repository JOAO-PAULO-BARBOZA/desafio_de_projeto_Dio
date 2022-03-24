import socket

conexao = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print('Socket criado com sucesso!')

host = 'localhost'
porta = 5432


conexao.bind((host, porta))

menssagem = "\nServidor: Hi client, yes I'm here"


while True:
    
    dados, endereco = conexao.recvfrom(4096)
    
    if dados:
        print('Servidor enviando menssagem...')
        conexao.sendto(dados + (menssagem.encode()), endereco)


