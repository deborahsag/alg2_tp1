import math


def menor_distancia(Ci, Cj):
    """Retorna os pontos de menor distancia entre dois conjuntos de pontos.

    Entrada:
    Ci, Cj - conjuntos de pontos (list de list)
    Saida:
    min_i, min_j - pontos de menor distancia (list)
    """
    min_i = Ci[0]
    min_j = Cj[0]
    min_dist = math.dist(min_i, min_j)
    for i in range(len(Ci)):
        pi = Ci[i]
        for j in range(len(Cj)):
            pj = Cj[j]
            d = math.dist(pi, pj)
            if d < min_dist:
                min_dist = d
                min_i = pi
                min_j = pj

    return min_i, min_j