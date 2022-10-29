#Função "direcao" verifica a direção relativa entre 3 pontos e é usada na função "interceptam"
def direcao(p1, p2, p3):
        
#Função "sobre_segmento" verifica se um ponto está sobre um segmento formado por outros dois pontos
def sobre_segmento(p1, p2, p3):

# Função "interceptam" para ver se dois segmentos se interceptam
def interceptam(p1, p2, p3, p4):
    d1 = direcao(p3, p4, p1)
    d2 = direcao(p3, p4, p2)
    d3 = direcao(p1, p2, p3)
    d4 = direcao(p1, p2, p4)
    if ((d1>0 and d2<0) or (d1<0 and d2>0)) and ((d3>0 and d4<0) or (d3<0 and d4>0)):
        return True
    elif d1==0 and sobre_segmento(p3, p4, p1):
        return True
    elif d2==0 and sobre_segmento(p3, p4, p2):
        return True
    elif d3==0 and sobre_segmento(p1, p2, p3):
        return True
    elif d4==0 and sobre_segmento(p1, p2, p4):
        return True
    else:
        return False

#Função "segmentos_interceptam" usa a função "interceptam" para ver se dois segmentos vizinhos da árvos T se interceptam

#Função "varredura_linear" usa a função "segmentos_interceptam" para ver se há interseção em um conjunto de segmentos