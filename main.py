import matplotlib.pyplot as plt

def histograma(a, p): # (fonte, alfabeto)
    # calcula o histograma
    histo = {}
    for letra in p:
        if letra in a:
            if letra in histo:
                histo[letra] += 1
            else:
                histo[letra] = 1

    print(histo)

    # mostra o histograma gráfico
    plt.bar(histo.keys(), histo.values())
    plt.show()

a = 'abcdefghijklmnopqrstuvwxyz'
p = 'aaaaaaaabbbcccdddeeefffggghhhiii'

histograma(a, p)


#! vvv Ignorar vvv 
#* 3 - aplicar a todas as fontes (img, text, wav)
#* 0 - 255 (cada elemento - 1 byte : num medio por simbolo 8 bits)
#* estudar o quanto é que nós conseguimos comprimir (valor mais baixo que teóricamente conseguimos atingir)