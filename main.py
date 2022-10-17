from typing import Counter
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from scipy.io import wavfile
import numpy as np

from Classes.huffmancodec import *

#! ex 1
def histograma(a, fonte, src): # (alfabeto, fonte, src)
    histo = {letra: 0 for letra in a}
    fonte = Counter(fonte)
    
    for letra in fonte:
        if letra in a: # não necessário pois o alfabeto já é o conjunto de letras da fonte
            histo[letra] = fonte[letra]

    # mostra o histograma gráfico
    plt.title(src)
    plt.bar(histo.keys(), histo.values())
    
    # abre janela maximizada
    mng = plt.get_current_fig_manager()
    mng.resize(*mng.window.maxsize())

    plt.show()

    return histo # return dicionário

#! ex 2
def entropia(histo, fonte):
    # remove todos os zeros dos valores do histograma no caso de existirem
    if 0 in histo.values():
        histo = {k: v for k, v in histo.items() if v != 0}

    p_i = np.array(list(histo.values()))/len(fonte)

    return -np.sum(p_i*np.log2(p_i))


#! ex 3
def getFonte(src):
    if src.endswith('.bmp'):
        fonte = mpimg.imread(src).flatten()
    elif src.endswith('.wav'):
        [temp, fonte] = wavfile.read(src)
    elif src.endswith('.txt'):
        fonte = open('./src/lyrics.txt', 'r').read()
        fonte = [i for i in fonte if i.isalpha()] # remove todos os caracteres que não são letras (não é optimizado)
    return fonte

def analyseFile(src):
    fonte = getFonte(src)
    a = [i for i in range(256)] if not src.endswith('.txt') else [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)]

    src = src.replace('./src/', '')
    histo = histograma(a, fonte, src)
    print(f"Entropia {src}: {entropia(histo, fonte)}")

#! ex 4
def analyseHuffman(src):
    fonte = getFonte(src)
    codec = HuffmanCodec.from_data(fonte)
    t = codec.get_code_table()
    # print(t)
    symbols, lenght = codec.get_code_len()
    # print(symbols)
    # print(lenght)
    media = sum(lenght)/len(lenght)
    print(f"Media: {media}\n")

#! ex 5
def analyseFilePairs(src):
    fonte = getFonte(src)
    fonte = [str(fonte[i]) + str(fonte[i+1]) for i in range(0, len(fonte)-1, 2)] # demora um bocadinho lol

    # gera alfabeto com todos os pares possíveis
    a = [] if not src.endswith('.txt') else [chr(i) + chr(j) for i in range(65, 91) for j in range(65, 91) ] + [chr(i) + chr(j) for i in range(97, 123) for j in range(97, 123) if i != j]

    # print(a)
    # print(fonte)

    src = src.replace('./src/', '')
    histo = histograma(a, fonte, src)
    print(histo)
    # print(f"Entropia {src}: {entropia(histo, fonte)}")


#!              ------   Main    ------
def main():
    files = ['./src/landscape.bmp', './src/MRI.bmp', './src/MRIbin.bmp', './src/soundMono.wav', './src/lyrics.txt']
    for file in files:
        analyseFile(file)
        # analyseHuffman(file)
        pass
    # analyseFilePairs('./src/lyrics.txt')

main()