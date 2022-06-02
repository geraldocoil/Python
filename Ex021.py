import pygame
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('audio021.mp3')
pygame.mixer.music.play(loops=0,start=0.0)
input('deseja parar? digite sim:')
pygame.event.wait()



