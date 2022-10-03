def histograma(p, a): # (fonte, alfabeto)
    histo = {}
    for letra in p:
        if letra in a:
            if letra in histo:
                histo[letra] += 1
            else:
                histo[letra] = 1
    return histo

a = 'abcdefghijklmnopqrstuvwxyz'

p = 'aaaaaaaabbbcccdddeeefffggghhhiii'

print(histograma(p, a))

# 3 - aplicar a todas as fontes
#Hello