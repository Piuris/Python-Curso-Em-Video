'''Faça um programa que abra e reproduza o áudio de um arquivo MP3'''
import pygame

pygame.init()
pygame.mixer.music.load("desafio021.wav")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)
