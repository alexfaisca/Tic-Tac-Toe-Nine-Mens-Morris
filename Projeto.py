def eh_tabuleiro(tab):
    correto = 0
    if type(tab) is tuple and len(tab) == 3:
        for i in tab:
            if type(i) is tuple and len(i) == 3:
                for element in i:
                    if type(element) is int and element < 2 and element > -2:
                        correto = correto + 1
                        if correto == 9:
                            return True
                        else:
                            continue
                    else:
                        return False
            else:
                return False
    else: 
        return False

def eh_posicao(x):
    if isinstance(x, int):
        if x < 10 and x > 0:
            return True
        else:
            return False
    else:
        return False

def obter_coluna(tab, coluna):
    if eh_tabuleiro(tab) and isinstance(coluna, int):
        if coluna <= len(tab) and coluna > 0:
            return(tuple(tab[i][coluna-1] for i in range(len(tab)))) 
    raise ValueError ('obter coluna: algum dos argumentos e invalido')
    
def obter_linha(tab, linha):
    if eh_tabuleiro(tab) and isinstance(linha, int):
        if linha <= len(tab) and linha > 0:
            return(tab[linha-1]) 
    raise ValueError ('obter linha: algum dos argumentos e invalido')

def obter_diagonal(tab, diagonal):
    if eh_tabuleiro(tab) and isinstance(diagonal, int):
        if diagonal == 1:
            return(tuple(tab[i][i] for i in range(len(tab)))) 
        elif diagonal == 2:
            return(tuple(tab[2 - i][i] for i in range(len(tab))))
    raise ValueError ('obter linha: algum dos argumentos e invalido')
#recebe um inteiro representante do numero de jogador e retorna o caracter correspondente ao jogador
def cifra(x):
    tabela = {-1 : 'O', 0 : ' ', 1 : 'X'}
    return tabela[x]

def tabuleiro_str(tab):
    if eh_tabuleiro(tab):
        tabuleiro_str = ''
        for i in range(len(tab)):
            if i == 2:
                tabuleiro_str += '{0:^5} | {1:^5} | {2:^5}\n'.format(cifra(tab[i][0]), cifra(tab[i][1]), cifra(tab[i][2]))
            else:
                tabuleiro_str += '{0:^5} | {1:^5} | {2:^5}\n----------------------\n'.format(cifra(tab[i][0]), cifra(tab[i][1]), cifra(tab[i][2]))                
        return tabuleiro_str
    raise ValueError ('O argumento intorduzido não é um tabuleiro')

def converter_pos_coord(a):
    if type(a) is tuple:
        d = {(0, 0):1, (0, 1):2, (0, 2):3, (1, 0):4, (1, 1):5, (1, 2):6, (2, 0):7, (2, 1):8, (2, 2):9}
        return  d[(a[0], a[1])]
    elif type(a) is int:
        d = {1:(0, 0), 2:(0, 1), 3:(0, 2), 4:(1, 0), 5:(1, 1), 6:(1, 2), 7:(2, 0), 8:(2, 1), 9:(2, 2)}
        return d[a]

def eh_posicao_livre(tab, posicao):
    if eh_tabuleiro(tab) and eh_posicao(posicao):
        a, b = converter_pos_coord(posicao)
        if tab[a][b] == 0: 
            return True
        else: return False
    raise ValueError('eh_posicao_livre: algum dos argumentos e invalido')



def obter_posicoes_livres(tab):
    if eh_tabuleiro(tab):
        livre = []
        for linha in range(len(tab)):
            for elemento in range(len(tab[linha])):
                if tab[linha][elemento] == 0:
                    livre = livre + [(linha, elemento)]
        for i in range(len(livre)):
            livre[i] = converter_pos_coord((livre[i][0], livre[i][1]))
        return tuple(livre)
    raise ValueError ('eh_posicao_livre: algum dos argumentos e invalido')

def jogador_ganhador(tab):
    if eh_tabuleiro(tab):
        if obter_diagonal(tab, 1) == (1, 1, 1) or obter_diagonal(tab, 2) == (1, 1, 1):
            return 1
        elif obter_diagonal(tab, 1) == (-1, -1, -1) or obter_diagonal(tab, 2) == (-1, -1, -1):
            return -1
        for i in range(1, len(tab) + 1):
            if obter_coluna(tab, i) == (1, 1, 1) or obter_linha(tab, i) == (1, 1, 1):
                return 1
            elif obter_coluna(tab, i) == (-1, -1, -1) or obter_linha(tab, i) == (-1, -1, -1):
                return -1
        return 0        
        
    raise ValueError ('jogador_ganhador: o argumento e invalido')

def marcar_posicao(tab, jogador, posicao):
    if eh_tabuleiro(tab) and eh_posicao_livre(tab, posicao) and (jogador == 1 or jogador == -1):
        tab_provisorio = [ i for i in tab]
        coordenadas = converter_pos_coord(posicao)
        tab_provisorio[coordenadas[0]] = list(tab_provisorio[coordenadas[0]])
        tab_provisorio[coordenadas[0]][coordenadas[1]] = jogador
        tab_provisorio[coordenadas[0]] = tuple(tab_provisorio[coordenadas[0]])
        return tuple(tab_provisorio)
    raise ValueError ('marcar_posicao: algum dos argumentos e invalido')

def escolher_posicao_manual(tab):
    if eh_tabuleiro(tab):
        x = int(input('Turno do jogador. Escolha uma posicao livre: '))
        if eh_posicao_livre(tab, x):
            print(x)
            return
        raise ValueError ('escolher_posicao_manual: a posicao escolhida e invalida')
    raise ValueError ('esolher_posicao_manual: a posicao escolhida e invalida')

#recebe um tuplo de posicoes livres retorna lista com as coordenadas as posicoes livres
def converter_tuplo_lista(t):
    lista = [i for i in t]
    for i in range(len(lista)):
        lista[i] = [e for e in converter_pos_coord(lista[i])]
    return lista
#recebe um tuplo e um inteiro e retorna o numero de vezes que o inteiro surge no tuplo
def elementos_linha(tuplo, x):
    number = 0
    for element in tuplo:
        if x == element:
            number = number + 1
    return number

#determinar a existencia e as coordenadas de um movimento vitoria
#recebe um tuplo (coluna/linha/diagonal) e dois inteiros(numero do jogador/numero de linha, coluna ou diagonal)
#retorna um tuplo com o movimento vencedor e boolean indicando existencia de vitoria
def vencedor_coluna(coluna, x, i):
    total = elementos_linha(coluna, x)
    if total == 2:
        for j in range(len(coluna)):
            if coluna[j] == 0:
                return [j, i], True
    return [], False

def vencedor_linha(linha, x, i):
    total = elementos_linha(linha, x)
    if total == 2:
        for j in range(len(linha)):
            if linha[j] == 0:
                return[i, j], True
    return [], False

def vencedor_diagonal(diagonal, x, i):
    total = elementos_linha(diagonal, x)
    if total == 2:
        for j in range(len(diagonal)):
            if diagonal[j] == 0:
                if i == 1: return (j, j), True
                elif i == 2: return [2 - j, j], True 
    return [], False

def movimento_vitoria(tab, x):
    jogada_vit = []
    for i in range((len(tab))):
        linha = obter_linha(tab, i + 1)
        jogada_vit, parar = vencedor_linha(linha, x, i)
        if parar: return jogada_vit 
        coluna = obter_coluna(tab, i + 1)
        jogada_vit, parar = vencedor_coluna(coluna, x, i)
        if parar: return jogada_vit 
    for i in [1, 2]:
        diagonal = obter_diagonal(tab, i)
        jogada_vit, parar = vencedor_diagonal(diagonal, x, i)
        if parar: return jogada_vit 
    return []

def vitoria(tab, x):
    jogada = movimento_vitoria(tab, x)
    if jogada == []:
        return False
    else:
        jogada = (jogada[0], jogada[1])
        jogada = converter_pos_coord(jogada)
        tab2 = marcar_posicao(tab, x, jogada)
        return True, tab2
    
def bloqueio(tab, x):
    jogada = movimento_vitoria(tab, -x)
    if jogada == []:
        return False
    else:
        jogada = (jogada[0], jogada[1])
        jogada = converter_pos_coord(jogada)
        tab2 = marcar_posicao(tab, x, jogada)
        return True, tab2
    

def procura_intersecao(linha1, linha2, x):
    pecas_linha1 = elementos_linha(linha1, x)
    if pecas_linha1 == 1:
        livres_linha1 = elementos_linha(linha1, 0)
        if livres_linha1 == 2:
            pecas_linha2 = elementos_linha(linha2, x)
            if pecas_linha2 == 1:
                livres_linha2 = elementos_linha(linha2, 0)
                if livres_linha2 == 2:
                    return True
    return False

def intersecao_linha_coluna(tab, x):
    jogada_intersecao = []
    for i in range(len(tab)):
        linha = obter_linha(tab, i + 1)
        for j in range(len(tab)):
            coluna = obter_coluna(tab, j + 1)
            proceder = procura_intersecao(linha, coluna, x)
            if proceder: 
                coords_intersecao = (i, j)
                posicao_candidata = converter_pos_coord(coords_intersecao)
                if eh_posicao_livre(tab, posicao_candidata):
                    jogada_intersecao = jogada_intersecao + [coords_intersecao]
    return jogada_intersecao

def bifurcacao(tab, x):
    intersecoes = intersecao_linha_coluna(tab, x)
    if intersecoes == []:
        return False
    else:
        jogada = intersecoes[0]
        jogada = converter_pos_coord(jogada)
        tab2 = marcar_posicao(tab, x, jogada)
        return True, tab2

# percorrer linhas/colunas/diagonais em busca de linhas com duas posicoes livres
# retornar as coordenadas das posicoes livres
def adicionar_posicao(lista1, lista2):
    lista = list(set(lista1 + lista2))
    return lista
    
def elegivel_bloqueio_bifurcacao(linha, x):
    pecas = elementos_linha(linha, x)
    if pecas == 1:
        livres = elementos_linha(linha, 0)
        if livres == 2:
            return True
    return False

#procurar linhas/colunas/diagonais em que hajam duas posicoes livres e uma peca do jogador
#recebem um tabuleiro e o numero de jogador, retornam as posicoes livres nas condicoes de forcar defesa

def verificar_posicao(coordenadas, intersecoes_adv):
    for e in intersecoes_adv:
        if e == coordenadas:
            return True
    return False
                
def candidatos_linha(tab, numero_linha, intersecoes_adv):
    a, b = [], []
    x = 0
    for j in range(len(tab[numero_linha])):
        if tab[numero_linha][j] == 0:
            if verificar_posicao((numero_linha, j), intersecoes_adv):
                x = x + 1
                a = [(numero_linha, j)]
            else: b = b + [(numero_linha, j)]
    if x == 2: return []
    elif x == 1: return a
    elif x == 0: return b

def procurar_linhas(tab, x, intersecoes_adv):
    candidato = []
    for i in range(len(tab)):
        linha = obter_linha(tab, i + 1)
        if elegivel_bloqueio_bifurcacao(linha, x):
            candidato = candidato + candidatos_linha(tab, i, intersecoes_adv)
    return candidato

def candidatos_coluna(tab, numero_coluna, intersecoes_adv):
    a, b = [], []
    x = 0
    for j in range(len(tab)):
        if tab[j][numero_linha] == 0:
            if verificar_posicao((j, numero_coluna), intersecoes_adv):
                x = x + 1
                a = [(j, numero_coluna)]
            else: b = b + [(j, numero_coluna)]
    if x == 2: return []
    elif x == 1: return a
    elif x == 0: return b
    
def procurar_colunas(tab, x, intersecoes_adv):
    candidato = []
    for i in range(len(tab)):
        coluna = obter_colunas(tab, i + 1)
        if elegivel_bloqueio_bifurcacao(coluna, x):
            candidato = candidato + candidatos_coluna(tab, numero_coluna, intersecoes_adv)
    return candidato    

def candidatos_diagonal(tab, numero_diagonal, intersecoes_adv):
    a, b = [], []
    x = 0
    if numero_diagonal == 1:
        for j in range(len(tab)):
            if tab[j][j] == 0:
                if verificar_posicao((j, j), intersecoes_adv):
                    x = x + 1
                    a = [(j, j)]
                else: b = b + [(j, j)]
    elif numero_diagonal == 2:
        for j in range(len(tab)):
            if tab[2 - j][j] == 0:
                if verificar_posicao((2 - j, j), intersecoes_adv):
                    x = x + 1
                    a = [(2 - j, j)]
                else: b = b + [(2 - j, j)]        
    if x == 2: return []
    elif x == 1: return a
    elif x == 0: return b

def procurar_diagonais(tab, x, intersecoes_adv):
    candidato = []
    for i in [1, 2]:
        diagonal = obter_diagonal(tab, i)
        if elegivel_bloqueio_bifurcacao(diagonal, x):
            for j in range(len(diagonal)):
                candidato = candidato + candidatos_diagonal(tab, i, intersecoes_adv)
        return candidato  
    
def procurar_posicoes(tab, x, intersecoes_adv):
    candidato = []
    candidato = adicionar_posicao(candidato, procurar_linhas(tab, x, intersecoes_adv))
    candidato = adicionar_posicao(candidato, procurar_colunas(tab, x, intersecoes_adv))
    candidato = adicionar_posicao(candidato, procurar_diagonais(tab, x, intersecoes_adv))
    return candidato

# para que a defesa a uma posicao dandidata nao gere uma bifurcacao a outra posicao em linha nao pode ser bifurcacao
    
    
    
def bloqueio_bifurcacao(tab, x):
    intersecoes_adv = intersecao_linha_coluna(tab, -x)
    if len(intersecoes_adv) == 1:
        jogada = intersecoes_adv[0]
        jogada = converter_pos_coord(jogada)
        tab2 = marcar_posicao(tab, x, jogada)
        return True, tab2
    elif len(intersecoes_adv) >= 2:
        jogada = procurar_posicoes(tab, x, intersecoes_adv)[0]
        jogada = converter_pos_coord(jogada)
        tab2 = marcar_posicao(tab, x, jogada)
        return True, tab2
    return False


def acao(i):
    d = {1 : 'vitoria', 2 : 'bloqueio', 3 : 'bifurcacao', 4 : 'bloqueio_bifurcacao', 5 : 'centro', \
         6 : 'canto_oposto', 7 : 'canto_vazio', 8 : 'lateral_vazio'}
    return d[i]

def escolher_acoes(estrategia):
    if estrategia == 'basico': return [5, 7, 8]
    if estrategia == 'normal': return [1, 2, 5, 6, 7, 8]
    else: return [1, 2, 3, 4, 5, 6, 7, 8]    

def jogada_computador(tab, x, acoes):
    for i in acoes:
        tab_modificado = acao(i)(tab, x)
        if tab != tab_modificado: 
            return tab_modificado

def marcar_posicao_auto(tab, x, estrategia):
    acoes = escolher_acoes(estrategia)
    return jogada_computador(tab, x, acoes)
        
    
    
    
        
    