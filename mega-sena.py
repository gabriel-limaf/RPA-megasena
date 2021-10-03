import pyautogui
from time import sleep
import webbrowser
import random


def numeros_usuario():
    lista_manual = []
    while True:
        n1 = input('Informe os 6 numeros separados por virgula, ex: 10,20,30,40,50,60: ')
        n1 = n1.split(',')
        lista_manual.append(n1)
        print(n1)
        if len(n1) != 6:
            continue
        else:
            break
    lista_manual = sorted(lista_manual)
    lista_manual = str(lista_manual)
    lista_manual = lista_manual.replace('[', '').replace(']', '').replace("'", '')
    with open('numeros.txt', 'a') as arquivo:
        arquivo.write(lista_manual + '\n')
        arquivo.close()
    return lista_manual


def gerar_numeros():
    lista = []
    tamanho = 6
    entrada = range(1, 61)
    while len(lista) < tamanho:
        numeros = random.choice(entrada)
        if numeros not in lista:
            lista.append(numeros)
        else:
            continue
    lista = sorted(lista)
    lista = str(lista)
    lista = lista.replace('[', '').replace(']', '')
    with open('numeros.txt', 'a') as arquivo:
        arquivo.write(lista + '\n')
        arquivo.close()
    return lista


def apostar(lista):
    webbrowser.open('https://www.loteriasonline.caixa.gov.br/silce-web/?utm_source=site_loterias&utm'
                    '/_medium=cross&utm_campaign=loteriasonline&utm_term=mega#/termos-de-uso')
    sleep(10)
    sim_button = pyautogui.locateOnScreen('sim.png')
    pyautogui.moveTo(sim_button), sleep(1)
    pyautogui.click(sim_button), sleep(1)
    pyautogui.hotkey('pagedown'), sleep(3)
    mega_button = pyautogui.locateOnScreen('mega.png')
    pyautogui.moveTo(mega_button), sleep(1)
    pyautogui.click(mega_button), sleep(1)
    pyautogui.moveTo(900, 100), sleep(1)
    pyautogui.hotkey('pagedown'), sleep(1)
    pyautogui.hotkey('down'), sleep(1)
    pyautogui.hotkey('down'), sleep(1)
    pyautogui.hotkey('down'), sleep(1)
    pyautogui.hotkey('down'), sleep(1)
    num = lista.split(', ')
    print(num)
    for i in num:
        num_button = pyautogui.locateOnScreen(i + '.png')
        pyautogui.moveTo(num_button)
        pyautogui.click(num_button)
    sleep(2)
    pyautogui.hotkey('ctrl', 'f'), sleep(1)
    pyautogui.typewrite('Colocar'), sleep(3)
    pyautogui.hotkey('enter'), sleep(3)
    pyautogui.hotkey('esc'), sleep(3)
    pyautogui.hotkey('enter')


def jogar():
    jogo = 0
    while True:
        man_aut = int(input('Deseja jogar com seus numeros ou deixar o Python escolher pra vocÇe?: \n'
                            'Meus números: Digite 1\n'
                            'Números Python: Digite 2\n'))
        if man_aut not in [1, 2]:
            continue
        if man_aut == 2:
            while jogo <= 6:
                numeros = gerar_numeros()
                apostar(numeros)
                jogo = jogo + 1
                exit()
        if man_aut == 1:
            numeros = numeros_usuario()
            apostar(numeros)
            exit()


jogar()
