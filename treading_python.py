from threading import Thread
import time


def carro(velocidade, tipo):
    trajeto = 0
    while trajeto <= 100:
        print(f'''
                         
                            
                [][][]      Carro {tipo}
                  []
                [][][]    {trajeto} km
                  []      {velocidade} km/h                             
                  
        ''')
        
        trajeto += velocidade
        time.sleep(0.5)

t_carro_A = Thread(target=carro, args=[1, 'A'])
t_carro_B = Thread(target=carro, args=[1.5, 'B'])

t_carro_A.start()
t_carro_B.start()


