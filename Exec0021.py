# Faça um programa em python que abra e reproduza um arquivo de mp3

import pygame

pygame.init()
file = r'D:\Users\manof\Downloads\500 CLASSIC ROCK SONGS\007 - Pink Floyd - Comfortably Numb.mp3'
pygame.mixer.music.load(file)
pygame.mixer.music.play()
pygame.event.wait()
input()
