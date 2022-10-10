from typing import Counter
import matplotlib.pyplot as plt
import math
import matplotlib.image as mpimg
from scipy.io import wavfile
import numpy as np

#! ex 1
def histograma(a, fonte, src): # (alfabeto, fonte, src)
    histo = {letra: 0 for letra in a}
    fonte = Counter(fonte)
    
    for letra in fonte:
        if letra in a:
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
    entropia = 0

    # TODO: (histo[letra]/len(fonte))*math.log2(histo[letra]/len(fonte))
    entropia = sum([-(histo[letra]/len(fonte))*math.log2(histo[letra]/len(fonte)) for letra in histo if histo[letra] != 0])

    return abs(entropia) # return da entropia em modulo, porque em cima é calculado com valor negativo

#! ex 3
def analyseImage(src):
    a = [i for i in range(256)] # alfabeto com todos os caracters para .bmp

    img = mpimg.imread(src)
    fonte = img.flatten() # transforma a imagem em array

    src = src.replace('./src/', '')
    histo = histograma(a, fonte, src)
    print(f"\nEntropia {src.replace('./src/', '')}: {entropia(histo, fonte)}\n")

def analyseWav(src):
    a = [i for i in range(256)] # alfabeto de som no intervalo [-1, 1[ para .wav'

    [temp, data] = wavfile.read(src)
    
    src = src.replace('./src/', '')
    histo = histograma(a, data, src)
    print(f"Entropia {src.replace('./src/', '')}: {entropia(histo, data)}")

def analyseTxt(src):
    a = [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)] # alfabeto de a-zA-Z para .txt

    fonte = open('./src/lyrics.txt', 'r').read() # string com todo o texto

    src = src.replace('./src/', '')
    histo = histograma(a, fonte, src) # aqui vai percorrer a string como se fosse um array
    print(f"Entropia {src}: {entropia(histo, fonte)}")


#!              ------   Main    ------
def main():
    '''Section for .bmp files'''
    # landscape
    analyseImage('./src/landscape.bmp')

    # MRI
    analyseImage('./src/MRI.bmp')
    
    # MRIbin
    analyseImage('./src/MRIbin.bmp')

    '''Section for .wav files'''
    # soundMono
    analyseWav('./src/soundMono.wav')

    '''Section for .txt files'''
    # lyrics
    analyseTxt('./src/lyrics.txt')

main()