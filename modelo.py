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
    x = (pi.x + pj.x) / 2
    y = (pi.y + pj.y) / 2