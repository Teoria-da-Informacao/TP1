import matplotlib.pyplot as plt
import math

# ex 1
def histograma(a, p): # (fonte, alfabeto)
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
    a = 'abcdefghijklmnopqrstuvwxyz'
    p = 'aaaaaaaabbbbbccccddddddeeeeeeeeeffghhhiiiiiiiiiii'

    histograma(a, p)
    entropia(a, p)


main()

#! vvv Ignorar vvv 
#* 3 - aplicar a todas as fontes (img, text, wav)
#* 0 - 255 (cada elemento - 1 byte : num medio por simbolo 8 bits)
#* estudar o quanto é que nós conseguimos comprimir (valor mais baixo que teóricamente conseguimos atingir)