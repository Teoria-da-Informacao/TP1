from typing import Counter
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from scipy.io import wavfile
import numpy as np
from Classes.huffmancodec import *

#! ex 1
def histograma(a, fonte, title): # title é opcional para não mostrar o histograma gráfico
    histo = {letra: 0 for letra in a} # cria dicionário todo a 0
    fonte = Counter(fonte) # função que conta o número de vez de cada simbolo aparece (retorna dicionário)
    
    # faz com que o histograma tenha letras do alfabeto todo, mesmo que seja 0
    for letra in fonte:
        if letra in a:
            histo[letra] = fonte[letra]

    plt.title(title)
    plt.bar(histo.keys(), histo.values())
    plt.show()

#! ex 2
def entropia(fonte):
    count = np.array(list(Counter(fonte).values()), dtype=int) # valores todos do histograma (aqui não tem valores a 0)
    pi = np.divide(count, len(fonte))
    return -np.sum(pi*np.log2(pi)) # formula da entropia

#! ex 3
def getFonte(src):
    if src.endswith('.bmp'):
        fonte = mpimg.imread(src).flatten()
    elif src.endswith('.wav'):
        [temp, fonte] = wavfile.read(src)
    elif src.endswith('.txt'):
        fonte = open(src, 'r').read()
        fonte = [i for i in fonte if i.isalpha()] # remove todos os caracteres que não são letras
    return fonte

def getAlfabeto(src):
    if src.endswith('.bmp') or src.endswith('.wav'):
        return [i for i in range(256)]
    elif src.endswith('.txt'):
        return [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)] # gera array de A-Za-z

def analyseFile(src):
    fonte = getFonte(src)
    a = getAlfabeto(src)

    src = src.replace('./src/', '')
    histograma(a, fonte, src) # mostra só o gráfico
    print(f"Entropia de {src}: {entropia(fonte)}")

#! ex 4
def mediaP(ocorrencias, length): # Média ponderada
    return np.divide(np.sum(np.multiply(ocorrencias, length)), np.sum(ocorrencias))

def varianciaP(ocorrencias, length): # Variancia ponderada
    return np.divide(np.sum(np.multiply(ocorrencias, np.power(length, 2))), np.sum(ocorrencias)) - np.power(mediaP(ocorrencias, length), 2) # E(X²) - [E(X)]²

def analyseHuffman(src):
    fonte = Counter(getFonte(src))
    
    codec = HuffmanCodec.from_data(fonte)
    symbols, length = codec.get_code_len()

    # ordena as keys da fonte em relação symbols, deixa já como array apenas os valores porque é a unica coisa que é preciso
    ocorrencias = [fonte[k] for k in symbols]

    src = src.replace('./src/', '')
    print(f'Média ponderada de {src}: {mediaP(ocorrencias, length)}')
    print(f'Variancia ponderada de {src}: {varianciaP(ocorrencias, length)}')

#! ex 5
def getAlfabetoPairs(src):
    if src.endswith('.bmp') or src.endswith('.wav'):
        return [i for i in range(0, 2**16)] # cria o alfabeto possivel para números juntos 16 bits
    elif src.endswith('.txt'):
        # junta o char unicode para ficar com um novo número
        return [np.unicode_(chr(i)+chr(j)) for i in range(65, 91) for j in range(65, 91)] + [np.unicode_(chr(i)+chr(j)) for i in range(97, 123) for j in range(97, 123)]

def analyseFilePairs(src):
    fonte = getFonte(src)
    if src.endswith('.txt'):
        # junta caracteres pelo seu unicode que vai ser unico por cada junção
        fonte = [np.unicode_(fonte[i]+fonte[i+1]) for i in range(0, len(fonte)-1, 2)]
    else:
        # junta caracteres dando shift ao primeiro numero 8 bits os outro bits da direita são ocupados pelo segundo numero que depois dá apenas um número "original"
        fonte = [((fonte[i] << 8) + fonte[i+1]) for i in range(0, len(fonte) - 1, 2)]

    print(f"Entropia em pares de {src.replace('./src/', '')}: {entropia(fonte) / 2}")

#! ex 6
def mutalInformation(query, target, a, step):
    mutual = [] # array das funções mutuas que vai ser devolvido
    for i in range(0, len(target), step): # percorre-se loop de step em step no intervalo [0, len(target)[
        if i + len(query) > len(target): # prevente que o [i + len(query)] faça parte do array 'target'
            break

        x = query[np.isin(query, a)] # filtra os caracteres que não estão no alfabeto
        y = target[i:i+len(query)][np.isin(target[i:i+len(query)], a)] # filtra os caracteres que não estão no alfabeto
        xy = [((x[i] << 8) + y[i]) for i in range(0, len(x))] # junta os caracteres em pares

        mutual.append(entropia(x) + entropia(y) - entropia(xy)) # formula I(X,Y) = H(X) + H(Y) - H(X, Y)
    return np.array(mutual)

def evolucaoInformacaoMutua(info, title):
    plt.title(title.replace('./src/MI/', ''))
    plt.plot(info)
    plt.show()

#? Alinea A
def alineaA():
    query = np.array([2, 6, 4, 10, 5, 9, 5, 8, 0, 8])
    target = np.array([6, 8, 9, 7, 2, 4, 9, 9, 4, 9, 1, 4, 8, 0, 1, 2, 2, 6, 3, 2, 0, 7, 4, 9, 5, 4, 8, 5, 2, 7, 8, 0, 7, 4, 8, 5, 7, 4, 3, 2, 2, 7, 3, 5, 2, 7, 4, 9, 9, 6])
    alfabeto = [i for i in range(11)]
    passo = 1
    infoMutua = mutalInformation(query, target, alfabeto, passo)
    print(infoMutua)

#? Alinea B
def alineaB():
    query = np.hsplit(getFonte('./src/MI/saxriff.wav'), 2)[0].flatten() # e.g. [[1, 2], [1, 2], ...] > pega em todos os 1's
    passo = round(len(query) / 4)
    alfa = getAlfabeto('./src/MI/saxriff.wav')

    target01 = np.hsplit(getFonte('./src/MI/target01 - repeat.wav'), 2)[0].flatten() # e.g. [[1, 2], [1, 2], ...] > pega em todos os 1's
    infoMutua01 = mutalInformation(query, target01, alfa, passo)
    print(infoMutua01)
    evolucaoInformacaoMutua(infoMutua01, './src/MI/saxriff.wav')

    target02 = np.hsplit(getFonte('./src/MI/target02 - repeatNoise.wav'), 2)[0].flatten() # e.g. [[1, 2], [1, 2], ...] > pega em todos os 1's
    infoMutua02 = mutalInformation(query, target02, alfa, passo)
    print(infoMutua02)
    evolucaoInformacaoMutua(infoMutua02, './src/MI/saxriff.wav')

#? Alinea C
def infoMaximos(songs, query, alfa, passo):
    maximos = {song.replace('./src/MI/', ''): 0 for song in songs} # {'Song01':0, 'Song02':0, ...}
    for song in songs:
        target = getFonte(song)
        if len(target.shape) == 2: # verifica se target é um array com mais de uma dimensão (linhas, cols) > se tiver apenas (linhas) não passa
            target = np.hsplit(target, 2)[0].flatten() # e.g. [[1, 2], [1, 2], ...] > pega em todos os 1's
        infoMutua = mutalInformation(query, target, alfa, passo)
        maximos[song.replace('./src/MI/', '')] = np.max(infoMutua)

    maximos = {k: v for k, v in sorted(maximos.items(), key=lambda item: item[1], reverse=True)} # ordena maximos
    # sorted() ordena por ordem crescente, reverse=True ordena por ordem decrescente
    # key=lambda item: item[1] ordena por valor e não por chave, em que item[0] seria a chave e item[1] o valor
    # lambda é uma função anónima, que não tem nome, é usada uma vez e não é preciso ser definida

    return maximos


#!              ------   Main    ------
def main():
    files = ['./src/landscape.bmp', './src/MRI.bmp', './src/MRIbin.bmp', './src/soundMono.wav', './src/lyrics.txt']
    for file in files:
        analyseFile(file)
        analyseHuffman(file)
        analyseFilePairs(file)
        print('#################################')

    #? 6 alinea a)
    alineaA()
    print('#################################')

    #? 6 alinea b)
    alineaB()
    print('#################################')

    #? 6 alinea c)
    query = np.hsplit(getFonte('./src/MI/saxriff.wav'), 2)[0].flatten() # e.g. [[1, 2], [1, 2], ...] > pega em todos os 1's
    alfa = getAlfabeto('./src/MI/saxriff.wav')
    passo = round(len(query) / 4)
    songs = ['./src/MI/Song01.wav', './src/MI/Song02.wav', './src/MI/Song03.wav', './src/MI/Song04.wav', './src/MI/Song05.wav', './src/MI/Song06.wav', './src/MI/Song07.wav']
    print(infoMaximos(songs, query, alfa, passo))

main()
