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

def getAlfabeto(src):
    if src.endswith('.bmp'):
        return [i for i in range(256)]
    elif src.endswith('.wav'):
        return [i for i in range(256)]
    elif src.endswith('.txt'):
        return [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)]

def analyseFile(src):
    fonte = getFonte(src)
    a = getAlfabeto(src)

    src = src.replace('./src/', '')
    histo = histograma(a, fonte, src)
    print(f"Entropia {src}: {entropia(histo, fonte)}")

#! ex 4
def mediaP(ocorrencias, length):
    return np.divide(np.sum(np.multiply(ocorrencias, length)), np.sum(ocorrencias))

def varianciaP(ocorrencias, length):
    return np.divide(np.sum(np.multiply(ocorrencias, np.power(length, 2))), np.sum(ocorrencias)) - np.power(mediaP(ocorrencias, length), 2)

def analyseHuffman(src):
    fonte = Counter(getFonte(src))

    codec = HuffmanCodec.from_data(fonte)
    symbols, length = codec.get_code_len()


    # ordena as keys da fonte em relação symbols
    temp = {k: fonte[k] for k in symbols}
    fonte = temp

    print(fonte.keys())
    print(symbols)
    
    ocorrencias = np.array(list(fonte.values()))

    src.replace('./src/', '')

    print(f'Média ponderada de {src}: {mediaP(ocorrencias, length)}')
    print(f'Variancia ponderada de {src}: {varianciaP(ocorrencias, length)}')

#! ex 5
def getAlfabetoPairs(src):
    if src.endswith('.bmp'):
        return [i for i in range(0, 2**16)]
    elif src.endswith('.wav'):
        return [i for i in range(0, 2**16)]
    elif src.endswith('.txt'):
        return [np.unicode_(chr(i)+chr(j)) for i in range(65, 91) for j in range(65, 91)] + [np.unicode_(chr(i)+chr(j)) for i in range(97, 123) for j in range(97, 123)]

def histogramaPairs(fonte, src): # (alfabeto, fonte, src)
    fonte = Counter(fonte)
    a = getAlfabetoPairs(src)
    histo = {letra: 0 for letra in a}

    for letra in fonte:
        if letra in histo:
            histo[letra] = fonte[letra]

    # mostra o histograma gráfico
    plt.title(src)

    plt.bar(histo.keys(), histo.values())

    plt.xticks([]) # para de mostrar os valores do eixo x

    plt.show()

    return histo # return histograma (dicionario)

def analyseFilePairs(src):
    fonte = getFonte(src)
    if src.endswith('.txt'):
        fonte = [np.unicode_(fonte[i]+fonte[i+1]) for i in range(0, len(fonte)-1, 2)]
    else:
        fonte = [((fonte[i] << 8) + fonte[i+1]) for i in range(0, len(fonte) - 1, 2)]

    src = src.replace('./src/', '')
    histo = histogramaPairs(fonte, src)

    # print(f"Entropia {src}: {entropia(histo, fonte)}")

#!              ------   Main    ------
def main():
    files = ['./src/landscape.bmp', './src/MRI.bmp', './src/MRIbin.bmp', './src/soundMono.wav', './src/lyrics.txt']
    for file in files:
        # analyseFile(file)
        analyseHuffman(file)
        # analyseFilePairs(file)
        pass
    # analyseFilePairs('./src/soundMono.wav')

main()