import matplotlib.pyplot as plt
import math
import matplotlib.image as mpimg
from scipy.io import wavfile

# ex 1
def histograma(a, p): # (alfabeto, fonte)
    #! Versão 1 (não inicializa o dicionário com letras que não aparecem)
    # histo = {}
    # for letra in p:
    #     if letra in a:
    #         if letra in histo:
    #             histo[letra] += 1
    #         else:
    #             histo[letra] = 1

    #! Versão 2 (inicializa o dicionário com letras que não aparecem)
    histo = {letra: 0 for letra in a}
    for letra in p:
        if letra in a and letra in histo:
            histo[letra] += 1
            
    # mostra o histograma na consola
    print(histo)

    # mostra o histograma gráfico
    plt.bar(histo.keys(), histo.values())
    plt.show()


# ex 2
def entropia(a, p):
    entropia = 0

    for letra in p:
        if letra in a:
            entropia += ((1/len(p)) * math.log2(1/len(p)))

    # valor calculado em cima é negativo, mas nós queremos o módulo!!
    entropia = abs(entropia)

    # mostra o valor da entropia na consola
    print(entropia)


def main():
    # TODO: FIX ALPHABET URGENTLY
    # a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    # a = [chr(i) for i in range(256)]
    

    # landscape.bmp
    landscape = mpimg.imread('./src/landscape.bmp')
    p1 = []
    for pixel in landscape[1]:
        p1.append(chr(pixel))

    # MRI.bmp
    mri = mpimg.imread('./src/MRI.bmp')
    p2 = []
    for pixel in mri[0]:
        p2.append(chr(pixel))
    
    # MRIbin.bmp
    mri_bin = mpimg.imread('./src/MRIbin.bmp')
    p3 = []
    for pixel in mri_bin[0]:
        p3.append(chr(pixel))

    # soundMono.wav
    # alfabeto de som no intervalo [-1, 1[
    [fs, data] = wavfile.read('./src/soundMono.wav')
    p4 = []
    for frame in data:
        p4.append(chr(frame))

    # histograma(a, p4)
    # entropia(a, p1)


main()

#! vvv Ignorar vvv 
#* 3 - aplicar a todas as fontes (img, text, wav)
#* 0 - 255 (cada elemento - 1 byte : num medio por simbolo 8 bits)
#* estudar o quanto é que nós conseguimos comprimir (valor mais baixo que teóricamente conseguimos atingir)