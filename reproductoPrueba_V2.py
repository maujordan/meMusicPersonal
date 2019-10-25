import pygame
import random
import socket
import json


#Variable para identificar que el estado de "pista1" sea
#diferente al anterior
a="f"


server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('', 12000))

pygame.mixer.init(44100, -16, 1, 4096)
channel1 = pygame.mixer.Channel(0)
channel2 = pygame.mixer.Channel(1)
channel3 = pygame.mixer.Channel(2)
channel4 = pygame.mixer.Channel(3)


def elegir_sonido(color, x, y):
    global a
    pista1=color +x +y +".ogg"
    """ pista2=color2 +cordX2 +cordY2 +".ogg"
        pista3=color3 +cordX3 +cordY3 +".ogg"
        pista4=color4 +cordX4 +cordY4 +".ogg"
    """


    """
        print(pista1)
        print(pista2)
        print(pista3)
        print(pista4)
    """

    print(f"------a: {a}\n------pista1: {pista1}")
    if a != pista1:

        print("entramos al  if 1")
        print(pista1)
        sonido1= pygame.mixer.Sound(pista1)
        channel1.play(sonido1, loops=-1)


        a=pista1


"""
    if b != pista2:


        print("entramos al  if 2")
        sonido2= pygame.mixer.Sound(pista2)
        channel2.play(sonido2)
        b=pista2
"""

"""

    if c != pista3:

        print("entramos al  if 3")
        sonido3= pygame.mixer.Sound(pista3)
        channel3.play(sonido3)
        c=pista3
"""

"""    if d != pista4:

        print("entramos al  if 4")
        sonido4= pygame.mixer.Sound(pista4)
        channel4.play(sonido4)
        d=pista4
"""

a="global"

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
