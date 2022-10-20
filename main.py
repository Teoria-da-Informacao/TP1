import time
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

    return histo # return histograma (dicionario)

#! ex 2
def entropia(histo, fonte):
    # remove todos os zeros dos valores do histograma no caso de existirem
    if 0 in histo.values():
        histo = {k: v for k, v in histo.items() if v != 0}

    p_i = np.array(list(histo.values()))/len(fonte)

    return -np.nansum(p_i*np.log2(p_i))


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
def mediaP(ocorrencias, lenghts):
    return np.divide(np.sum(np.multiply(ocorrencias, lenghts)), np.sum(ocorrencias))

# TODO: variancia ponderada

def analyseHuffman(src):
    fonte = getFonte(src)
    ocorrencias = list(Counter(fonte).values())

    codec = HuffmanCodec.from_data(fonte)
    symbols, lenght = codec.get_code_len()

    media = mediaP(ocorrencias, lenght)
    print(media)

#! ex 5
'''
    * [0, 0, 2, 0, 1, 0 ,2 , 0, 0, 2, 0, 0]
    *   0 = 8/12
    *   1 = 1/12
    *   2 = 3/12
    ! juntar em de 2 bits
'''

def histogramaPairs(fonte, src): # (alfabeto, fonte, src)
    fonte = Counter(fonte)

    # mostra o histograma gráfico
    plt.title(src)

    plt.bar([(str(i[0])+', '+str(i[1])) for i in fonte.keys()], fonte.values())
    plt.xticks([])
    plt.show()

    return fonte # return histograma (dicionario)

def analyseFilePairs(src):
    fonte = getFonte(src)
    fonte = np.array(fonte).reshape((-1, 2))
    fonte = tuple(map(tuple, fonte))

    src = src.replace('./src/', '')
    histo = histogramaPairs(fonte, src)


    # print(f"Entropia {src}: {entropia(histo, fonte)}")


#!              ------   Main    ------
def main():
    files = ['./src/landscape.bmp', './src/MRI.bmp', './src/MRIbin.bmp', './src/soundMono.wav', './src/lyrics.txt']
    for file in files:
        # analyseFile(file)
        # analyseHuffman(file)
        # analyseFilePairs(file)
        pass

main()