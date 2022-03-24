'''BIBLIOTECA USADA PARA MANIPULAR ENDEREÇOS IP's E DE REDE'''
import ipaddress

ip = '192.168.0.0' # criação de um ip em str.

endereco = ipaddress.ip_address(ip) # instanciação de um objeto que modifica a str transformando-a em um ip.

print(f'O endereço {endereco} é do tipo {type(endereco)}')

numero_de_ips = int(input('Informe quantos ips serão adicionados: '))

soma = endereco + numero_de_ips 

print(f'Soma do ip 192.168.0.0: {soma}' )

print(type(numero_de_ips))

rede = '192.168.0.0/24'

end_rede = ipaddress.ip_network(rede)


for ip in end_rede:
    print(ip)

