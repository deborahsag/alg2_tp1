from envoltoria import *
        
#Função "sobre_segmento" verifica se um ponto está sobre um segmento formado por outros dois pontos
#Entrada: lista de pontos [x, y]
def sobre_segmento(p1, p2, p3):
    #Verifica se o ponto p3 está dentro do intervalo do seguimento definido por p1 e p2
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

#Função "segmentos_interceptam" usa a função "interceptam" para ver se dois segmentos vizinhos da árvos T se interceptam

#Função "varredura_linear" usa a função "segmentos_interceptam" para ver se há interseção em um conjunto de segmentos