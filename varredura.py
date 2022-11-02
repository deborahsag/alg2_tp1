from http.client import INSUFFICIENT_STORAGE
from envoltoria import *
from queue import PriorityQueue

class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print_ponto(self):
        print(self.x, self.y)


def print_pontos(pontos):
    for p in pontos:
        p.print_ponto()

def lista_pontos(S):
    """Transforma uma lista de pontos representados por tuplas em uma lista da classe Ponto.
    
    Entrada:
    S - uma lista de pontos representados por tuplas
    Saida:
    pontos - uma lista de elementos da classe Ponto
    """
    pontos = []
    for i in range(len(S)):
        pontos.append(Ponto(S[i][0], S[i][1]))
    return pontos

class Segmento:
    def __init__(self, ponto1, ponto2):
        self.inicio = ponto1
        self.fim = ponto2 
    
    def ocorrencia(self, ponto):
        if self.inicio == ponto:
            o = "inicio"
            return o
        else: 
            o = "fim"
            return o

def lista_segmentos(L):
    segmentos = []
    for i in range(len(L)):
        segmentos.append(Segmento(L[i], L[i+1]))
    return segmentos

class Evento:
    def __init__(self, ponto, posicao, indice):
        self.ponto = ponto
        self.posicao = posicao
        self.indice = indice
    #é um ponto, inicio ou fim
    #índice do vetor de segmentos
    #ordenar eventos pela coordenada x e andar sob eles, se for início coloca segmento na árvola, ordenando pelo valor de y do ponto inicio e vai fazendo o algoritmo

def lista_eventos(L):
    #Entrada é lista_segmentos
    eventos = []
    for i in range(len(L)):
        a = i.inicio
        b = i.fim
        o1 = a.ocorrencia
        o2 = b.ocorrencia
        eventos.append(Evento(a, o1, i))
        eventos.append(Evento(b, o2, i))
    return eventos

#Função "sobre_segmento" verifica se um ponto está sobre um segmento formado por outros dois pontos
#Entrada: lista de pontos [x, y]
def sobre_segmento(p1, p2, p3):
    #Verifica se o ponto p3 está dentro do intervalo do segmento definido por p1 e p2
    if((p1[0] <= p3[0]) and (p3[0] <= p2[0])) and (((p1[1] <= p3[1]) and (p3[1] <= p2[1])) or ((p1[1] >= p3[1]) and (p3[1] >= p2[1]))):
        return True
    else:
        return False

# Função "interceptam" para ver se dois segmentos se interceptam
def interceptam(p1, p2, p3, p4):
    d1 = orientacao(p3, p4, p1)
    d2 = orientacao(p3, p4, p2)
    d3 = orientacao(p1, p2, p3)
    d4 = orientacao(p1, p2, p4)
    #Verifica se houve mudança de orientação
    if ((d1==1 and d2==2) or (d1==2 and d2==1)) and ((d3==1 and d4==2) or (d3==2 and d4==1)):
        return True
    #Se não houve mudança de orientação
    elif d1==0 and sobre_segmento(p3, p4, p1):
        #Verifica se p1 está sobre o segmento formado por p3 e p4
        return True
    elif d2==0 and sobre_segmento(p3, p4, p2):
        #Verifica se p2 está sobre o segmento formado por p3 e p4
        return True
    elif d3==0 and sobre_segmento(p1, p2, p3):
        #Verifica se p3 está sobre o segmento formado por p1 e p2
        return True
    elif d4==0 and sobre_segmento(p1, p2, p4):
        #Verifica se p4 está sobre o segmento formado por p1 e p2
        return True
    else:
        return False

#Função "segmentos_interceptam" usa a função "interceptam" para ver se dois segmentos vizinhos da árvore T se interceptam
def segmentos_interceptam()

#Função "varredura_linear" usa a função "segmentos_interceptam" para ver se há interseção em um conjunto de segmentos
def varredura_linear (pontos):
    segmentos = lista_segmentos(envoltoria_convexa(pontos))
    eventos = lista_eventos(segmentos)
    
    #inicializar árvore vazia

#inserir segmento na AVL, n o evento