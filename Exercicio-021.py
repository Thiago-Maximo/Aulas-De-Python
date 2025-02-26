# Faça um programa que abra e reproduza um audio de arquivo mp3

import pygame
pygame.init()
pygame.mixer.music.load('monaco.mp3')
pygame.mixer.music.play()
pygame.event.wait()