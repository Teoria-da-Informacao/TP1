from typing import Counter
import matplotlib.pyplot as plt
import math
import matplotlib.image as mpimg
from scipy.io import wavfile
import numpy as np

#! ex 1
def histograma(a, p, src): # (alfabeto, fonte)
    histo = {letra: 0 for letra in a}
    for letra in p:
        if letra in a and letra in histo:
            histo[letra] += 1

    '''print(histo) # mostra o histograma na consola como se fosse dicionário'''

    # mostra o histograma gráfico
    plt.title(src)
    plt.bar(histo.keys(), histo.values())
    
    # Esconde label x
    # plt.xticks([])
    # plt.yticks([letra for letra in histo if histo[letra] > 0])

    # abre janela maximizada
    mng = plt.get_current_fig_manager()
    mng.resize(*mng.window.maxsize())

    plt.show()

    return histo # return dicionário

#! ex 2
def entropia(histo, p):
    entropia = 0

    for letra in histo:
        if histo[letra] != 0:
            entropia += ((histo[letra] / len(p)) * math.log2(histo[letra] / len(p)))

    return abs(entropia) # return da entropia em modulo, porque em cima é calculado com valor negativo

#! ex 3
def analyseImage(src):
    a = [chr(i) for i in range(256)] # alfabeto com todos os caracters para .bmp

    img = mpimg.imread(src)
    p = [chr(pixel) for pixel in img[0]] # põe cada pixel convertido para caracter no array

    src = src.replace('./src/', '')
    histo = histograma(a, p, src)
    print(f"\nEntropia {src.replace('./src/', '')}: {entropia(histo, p)}\n")

def analyseWav(src):
    #TODO: not sure mas se for este o alfabeto então não está a funcionar como deveria
    # a = [i/100 for i in range(-100, 100)] # alfabeto de som no intervalo [-1, 1[ para .wav
    # np.arrange

    [temp, data] = wavfile.read(src)
    data = data / np.iinfo(data.dtype).max # normaliza os dados para o intervalo [-1, 1[
    d = (1 - (-1)) / (2**data.itemsize)
    a = np.arange(-1, 1, d)
    
    print(a)
    print('------')
    print(data)
    
    src = src.replace('./src/', '')
    histo = histograma(a, data, src)
    print(f"Entropia {src.replace('./src/', '')}: {entropia(histo, data)}")

def analyseTxt(src):
    a = [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)] # alfabeto de a-zA-Z para .txt

    p = open('./src/lyrics.txt', 'r').read() # string com todo o texto

    src = src.replace('./src/', '')
    histo = histograma(a, p, src) # aqui vai percorrer a string como se fosse um array
    print(f"Entropia {src}: {entropia(histo, p)}")


#!              ------   Main    ------
def main():
    '''Section for .bmp files'''
    # landscape
    # analyseImage('./src/landscape.bmp')

    # MRI
    # analyseImage('./src/MRI.bmp')
    
    # MRIbin
    # analyseImage('./src/MRIbin.bmp')

    '''Section for .wav files'''
    # TODO: Make alphabet for wav files
    # soundMono
    analyseWav('./src/soundMono.wav')

    '''Section for .txt files'''
    # lyrics
    # analyseTxt('./src/lyrics.txt')

main()