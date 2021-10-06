import pyautogui
from time import sleep
import webbrowser
import random
import pyperclip


def num_conc():
    conc = input('Qual o numero do concurso que deseja jogar ou conferir o jogo?: ')
    return conc


def numeros_usuario(conc):
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
    with open(conc + 'numeros_manual.txt', 'a') as arquivo:
        arquivo.write(lista_manual + '\n')
        arquivo.close()
    return lista_manual


def gerar_numeros(conc):
    lista = []
    tamanho = 6
    entrada = range(1, 61)
    while len(lista) < tamanho:
        numeros = random.choice(entrada)
        numeros = str(numeros).zfill(2)  # transformei em string para colocar 0 a esquerda
        if numeros not in lista:
            lista.append(numeros)
        else:
            continue
    lista = sorted(lista)
    lista = str(lista)
    lista = lista.replace('[', '').replace(']', '').replace("'", '')
    with open(conc + 'numeros_python.txt', 'a') as arquivo:
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


def numero_sorteado(conc):
    contador = 0
    webbrowser.open('http://loterias.caixa.gov.br/wps/portal/loterias/landing/megasena/')
    sleep(3)
    buscar_button = pyautogui.locateOnScreen('buscar.png')
    pyautogui.moveTo(buscar_button), sleep(1)
    pyautogui.click(buscar_button), sleep(1)
    pyautogui.hotkey('tab'), sleep(1)
    pyautogui.typewrite(conc), sleep(1)
    pyautogui.hotkey('enter'), sleep(1)
    pyautogui.click(), sleep(1)
    sleep(4)
    pyautogui.hotkey('ctrl', 'a')
    sleep(1)
    pyautogui.hotkey('ctrl', 'c')
    var = pyperclip.paste()
    sleep(3)
    arquivo = open('extracao-site.txt', 'w+', encoding="utf-8")
    arquivo.writelines(var)
    with open('extracao-site.txt', "r", encoding="utf-8") as arquivo:
        file = arquivo.readlines()
        for concurso in file:
            contador = contador + 1
            if 'Sorteio realizado' in concurso:
                break
    with open('extracao-site.txt', "r", encoding="utf-8") as arquivo:
        num = arquivo.readlines()[contador + 3]
    print('O número sorteado foi o: ' + num)  # numero sorteado
    return num


def conferir_numeros(num, conc):
    contador = 0
    num = num.replace(' ', '')
    with open(conc + 'numeros_python.txt', "r") as arquivo:
        file = arquivo.readlines()
        for meus_numeros in file:
            x = meus_numeros.replace(', ', '')
            print('Você jogou o número: ' + x, end='')
            contador = contador + 1
            if num in x:
                print(f'VOCE É UM GANHADOR DA MEGASENA !! Acertou na linha {contador}\n')
                break
            else:
                print('Infelizmente não foi desta vez !\n')


def jogar():
    jogo = 0
    while True:
        man_aut = int(input('Deseja jogar com seus numeros ou deixar o Python escolher para você?: \n'
                            'Meus números: Digite 1\n'
                            'Números Python: Digite 2\n'
                            'Conferir jogos: Digite 3\n'
                            'Sair: Digite 4\n'))
        if man_aut not in [1, 2, 3, 4]:
            continue
        if man_aut == 2:
            conc = num_conc()
            while jogo <= 6:
                numeros = gerar_numeros(conc)
                apostar(numeros)
                jogo = jogo + 1
            exit()
        if man_aut == 1:
            conc = num_conc()
            numeros = numeros_usuario(conc)
            apostar(numeros)
            exit()
        if man_aut == 3:
            conc = num_conc()
            num = numero_sorteado(conc)
            conferir_numeros(num, conc)
            exit()
        if man_aut == 4:
            exit()


jogar()
