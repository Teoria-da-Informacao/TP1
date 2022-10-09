import matplotlib.pyplot as plt
import math
import matplotlib.image as mpimg
from scipy.io import wavfile

#! ex 1
def histograma(a, p): # (alfabeto, fonte)
    histo = {letra: 0 for letra in a}
    for letra in p:
        print(letra, end='')
        if letra in a and letra in histo:
            histo[letra] += 1
            
    # mostra o histograma na consola
    print(histo)

    # mostra o histograma gráfico
    plt.bar(histo.keys(), histo.values())
    plt.show()


#! ex 2
def entropia(a, p):
    entropia = 0

    for letra in p:
        if letra in a:
            entropia += ((1/len(p)) * math.log2(1/len(p)))

    return abs(entropia) # return da entropia em modulo, porque em cima é calculado com valor negativo

#! ex 3
def analyseImage(src):
    a = [chr(i) for i in range(256)] # alfabeto com todos os caracters para .bmp

    img = mpimg.imread(src)
    p = [chr(pixel) for pixel in img[0]] # põe cada pixel convertido para caracter no array

    histograma(a, p)
    print(f"Entropia {src.replace('./src/', '')}: {entropia(a, p)}")

def analyseWav(src):
    #TODO: not sure mas se for este o alfabeto então não está a funcionar como deveria
    '''a = [i/100 for i in range(-100, 100)] # alfabeto de som no intervalo [-1, 1[ para .wav'''

    a = []

    [temp, data] = wavfile.read(src)
    # possivelmente depois dar delete ao temp >>> del temp 
    p = [chr(frame) for frame in data] # põe cada frame convertido para caracter no array
    
    histograma(a, p)
    print(f"Entropia {src.replace('./src/', '')}: {entropia(a, p)}")

def analyseTxt(src):
    a = [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)] # alfabeto de a-zA-Z para .txt

    p = open('./src/lyrics.txt', 'r').read() # string com todo o texto

    histograma(a, p) # aqui vai percorrer a string como se fosse um array
    print(f"Entropia {src.replace('./src/', '')}: {entropia(a, p)}")


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
    # TODO: Make alphabet for wav files
    # soundMono
    analyseWav('./src/soundMono.wav')

    '''Section for .txt files'''
    # lyrics
    analyseTxt('./src/lyrics.txt')

main()