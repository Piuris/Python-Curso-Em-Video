'''Crie um código em Python que teste se o site Pudim está acessível pelo
computador usado.'''
import requests


def verificar(url):
    try:
        resp = requests.get(url)
        resp.raise_for_status()
        print(f'O site {url} está acessível')
    except requests.RequestException:
        print(f'O site {url} não está acessível.')


url = "https://www.pudim.com.br"
verificar(url)
