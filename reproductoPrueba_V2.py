import pygame
import random
import socket
import json


#Variable para identificar que el estado de "pista1" sea
#diferente al anterior



server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('', 12000))

pygame.mixer.init(44100, -16, 1, 4096)
channel1 = pygame.mixer.Channel(0)
channel2 = pygame.mixer.Channel(1)
channel3 = pygame.mixer.Channel(2)
channel4 = pygame.mixer.Channel(3)


def elegir_sonido(color, x, y):
    global a
    a="variable_global"

    if x[0]==1:
        if y[0] != '-':
            pista1="audios/"+color +"-" +x[1] +y[0] +".ogg"
            
        
    if x[0] != '-':
        if y[0] =='-':
            pista1="audios/"+color +x[0] +"-" +y[1] +".ogg"
        

    if x[0] == '-':
        if y[0]== '-':
            pista1="audios/"+color +"-" +x[1] +"-" +y[1] +".ogg"
            
        
    else:
        pista1="audios/"+color +x[0] +y[0] +".ogg"
            
  


  

    #print(f"------a: {a}\n------pista1: {pista1}")
   
        
    if a != pista1:

        print(pista1)
        sonido1= pygame.mixer.Sound(pista1)
        channel1.play(sonido1, loops=-1)
        a=pista1



while True:
    rand = random.randint(0, 10)
    message, address = server_socket.recvfrom(1024)

    message = message.decode('utf-8')
    data = json.loads(message)

    #print('color: {}'.format(data['color']))
    #print('x: {}, y: {}'.format(data['x'], data['y']))

    color='{}'.format(data['color'])
    x='{}'.format(data['x'])
    y='{}'.format(data['y'])

    elegir_sonido(color, x, y)



#pygame.mixer.music.load(eleccion)
#sound1 = pygame.mixer.Sound('')

#channel2 = pygame.mixer.Channel(1)
#sound2 = pygame.mixer.Sound('file_example2.ogg')
#channel2.play(sound2)
