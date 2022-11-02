import math

from envoltoria import *


def menor_distancia(Ci, Cj):
    """Retorna os pontos de menor distancia entre dois conjuntos de pontos.

    Entrada:
    Ci, Cj - conjuntos de pontos (classe Ponto)
    Saida:
    min_i, min_j - pontos de menor distancia (classe Ponto)
    """
    min_i = Ci[0]
    min_j = Cj[0]
    min_dist = math.dist([min_i.x, min_i.y], [min_j.x, min_j.y])
    for i in range(len(Ci)):
        pi = Ci[i]
        for j in range(len(Cj)):
            pj = Cj[j]
            d = math.dist([pi.x, pi.y], [pj.x, pj.y])
            if d < min_dist:
                min_dist = d
                min_i = pi
                min_j = pj

    return min_i, min_j

def ponto_medio(pi, pj):
    """Retorna o ponto medio de um segmento de reta.
    
    Entrada:
    pi, pj - pontos da classe ponto
    Saida:
    p - o ponto medio do segmento pi-pj
    """
    x = (pi.x + pj.x) / 2
    y = (pi.y + pj.y) / 2
    p = Ponto(x, y)
    return p


def inclinacao(pi, pj):
    """Retorna a inclinacao da reta que passa por dois pontos.
    
    Entrada:
    pi, pj - pontos da classe Ponto
    Saida:
    slope - inclinacao da reta que passa por pi e pj
    """
    yd = pj.y - pi.y
    xd = pj.x - pi.x
    if xd == 0:
        return 0.1
    slope = yd / xd
    return slope


def equacao_modelo(Ci, Cj):
    """Retorna a equacao do modelo dadas duas envoltorias convexas.
    
    Entrada:
    Ci, Cj - envoltorias convexas (lists da classe Ponto)
    Saida:
    a - coeficiente angular da reta
    b - coeficiente linear da reta
    """
    pi, pj = menor_distancia(Ci, Cj)
    slope = inclinacao(pi, pj)
    pm = ponto_medio(pi, pj)
    a = - 1 / slope
    b = pm.y - a * pm.x
    return a, b


def classificador(p, a, b):
    linha = a * p.x + b
    if p.y > linha:
        return 'blue'
    elif p.y < linha:
        return 'red'
    else:
        return None     # o ponto esta exatamente em cima da linha e deve ser descartado