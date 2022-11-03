from envoltoria import *
from bintrees import *

class Segmento:
    #Um Segmento tem um ponto inicial e um ponto final
    def __init__(self, ponto1, ponto2):
        self.inicio = ponto1
        self.fim = ponto2 
    
    def ocorrencia(self, ponto):
        #Verifica se o ponto é incial ou final
        if self.inicio == ponto:
            o = "inicio"
            return o
        else: 
            o = "fim"
            return o

def lista_segmentos(L):
    #Cria uma lista de segmentos a partir de uma lista de pontos
    segmentos = []
    for i in range(len(L)):
        segmentos.append(Segmento(L[i], L[i+1]))
    return segmentos

class Evento:
    #Um evento é composto por um ponto, sua posição(inicio ou fim) e o índice do segmento ao qual ele pertence na lista de segmentos
    def __init__(self, ponto, posicao, indice):
        self.ponto = ponto
        self.posicao = posicao
        self.indice = indice

def lista_eventos(L):
    #Cria uma lista de eventos a partir de uma lista de segmentos
    eventos = []
    for i in range(len(L)):
        a = L[i].inicio
        b = L[i].fim
        o1 = a.ocorrencia
        o2 = b.ocorrencia
        eventos.append(Evento(a, o1, i))
        eventos.append(Evento(b, o2, i))
    return eventos

#Função "sobre_segmento" verifica se um ponto está sobre um segmento formado por outros dois pontos
def sobre_segmento(p1, p2, p3):
    #Verifica se o ponto p3 está dentro do intervalo do segmento definido por p1 e p2
    if((p1.x <= p3.x) and (p3.x <= p2.x)) and (((p1.y <= p3.y) and (p3.y <= p2.y)) or ((p1.y >= p3.y) and (p3.y >= p2.y))):
        return True
    else:
        return False

# Função "interceptam" para ver se dois segmentos se interceptam
def interceptam(segmento1, segmento2):
    p1 = segmento1.inicio
    p2 = segmento1.fim
    p3 = segmento2.inicio
    p4 = segmento2.fim
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

#Função "varredura_linear" usa a função "interceptam" para ver se há interseção em um conjunto de segmentos
#Entrada: lista de pontos retornada pela envoltória
def varredura_linear (lista_pontos):
    #Pega os segmentos da envoltória
    segmentos = lista_segmentos(lista_pontos)
    #Cria uma lista com os eventos dos segmentos da lista
    eventos = lista_eventos(segmentos)
    #Ordena os eventos pela coordenada x
    eventos = eventos.sort()
    #Cria uma árvore vazia
    T = AVLTree()
    #Percorre a lista de eventos
    for i in range(len(eventos)):
        j = eventos[i].indice
        #Se o evento for o início de um segmento, insere segmento na árvore e checa se há interseção 
        if eventos[i].posicao == "inicio":
            p = segmentos[j].inicio
            ind = p.y
            T.__setitem__(ind, segmentos[j])
            #checar se existe vizinho e se tem interseção
            #Se for o primeiro evento não haverá vizinhos
            if i == 0:
                break
            #ver se tem interseção com vizinho
            else:
                try: 
                    if (interceptam(T.prev_item(ind), T.__getitem__(ind))) or (interceptam(T.__getitem__(ind), T.succ_item(ind))):
                        r = True
                except:
                    print("Não tem vizinho")
                else: 
                    return r
        elif eventos[i].posicao == "fim":
            #Se o evento for o fim de um segmento, checa se seus vizinhos se interceptam e retira segmento da árvore
            #se os dois vizinhos do segmento existem e se interceptam
            try: 
                if (interceptam(T.prev_item(ind), T.succ_item(ind))):
                    r = True
            except:
                print("Não tem vizinho")
            else: 
                return r
            #deletar da árvore
            T.__delitem__(ind)
    return False