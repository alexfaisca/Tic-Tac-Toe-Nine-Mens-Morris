#Alexandre Faisca Coelho ist1100120
def eh_tabuleiro(tab):
    #universal -> bool
    '''recebe um universal tab se e tabuleiro devolve True, doutro modo Falso'''
    if type(tab) is tuple and len(tab) == 3: #verifica se tuplo e tamanho deste 
        for linha in tab: #para cada subtuplo repete o procedimento
            if type(linha) is tuple and len(linha) == 3:
                for elemento in linha: #verifica de cada elemento e valido
                    if (type(elemento) is not int) or \
                       (elemento > 1 or elemento < -1):
                        return False
            else:
                return False
    else: 
        return False
    return True #caso todas as condicoes se cumpram devolve True

def eh_posicao(x):
    #universal -> bool
    '''recebe universal x e devolve True se for posicao senao devolve False'''
    if type(x) is int and x < 10 and x > 0: # posicao e inteiro entre 1 e 9
        return True
    return False

def obter_coluna(tab, coluna):
    #tabuleiro x inteiro -> coluna
    '''recebe um tabuleiro tab e um inteiro coluna e devolve a coluna do
    tabuleiro correspondente ao inteiro'''
    if eh_tabuleiro(tab) and (type(coluna) is int) and 0 < coluna <= len(tab):
        return(tuple(tab[i][coluna-1] for i in range(len(tab))))  
    raise ValueError ('obter_coluna: algum dos argumentos e invalido')

def obter_linha(tab, linha):
    #tabuleiro x inteiro -> linha
    '''recebe um tabuleiro tab e um inteiro linha e devolve a linha do tabuleiro
    correspondente ao inteiro'''
    if eh_tabuleiro(tab) and (type(linha) is int) and 0 < linha <= len(tab):
        return(tab[linha-1])  
    raise ValueError ('obter_linha: algum dos argumentos e invalido')

def obter_diagonal(tab, diagonal):
    #tabuleiro x inteiro -> diagonal
    '''recebe um tabuleiro tab e um inteiro diagonal e devolve a diagonal do 
    tabuleiro correspondente ao inteiro'''
    if eh_tabuleiro(tab) and type(diagonal) is int:
        if diagonal == 1:
            return(tuple(tab[i][i] for i in range(len(tab)))) 
        elif diagonal == 2:
            return(tuple(tab[2 - i][i] for i in range(len(tab))))
    raise ValueError ('obter_diagonal: algum dos argumentos e invalido')


def cifra(x):
    #inteiro -> marca de jogador
    '''recebe um inteiro x devolve a marca de jogador correspondente'''
    tabela = {-1 : 'O', 0 : ' ', 1 : 'X'}
    return tabela[x]

def tabuleiro_str(tab):
    #tabuleiro -> string
    '''recebe um tabuleiro tab e devolve string que o representa visualmente'''
    if eh_tabuleiro(tab):
        tabuleiro_str = ''
        linha = ''
        for i in range(len(tab)): #determina a representacao das linhas de tab
            if i == len(tab) - 1: # terceira linha nao tem picotado
                linha = '{0:^3}|{1:^3}|{2:^3}'\
                    .format(cifra(tab[i][0]), cifra(tab[i][1]), cifra(tab[i][2]))
            else:
                linha = '{0:^3}|{1:^3}|{2:^3}\n-----------\n'\
                    .format(cifra(tab[i][0]), cifra(tab[i][1]), cifra(tab[i][2]))                
            tabuleiro_str += linha 
        return tabuleiro_str 
    raise ValueError ('tabuleiro_str: o argumento e invalido')

def converter_pos_coord(a):
    #coordenadas/posicao -> posicao/coordenadas
    '''recebe tuplo/inteiro a representando coordenadas/posicao e devolve um
    inteiro/tuplo com a posicao/coordenadas correspondente'''
    if type(a) is tuple: # se a for um par de coordenadas
        d = {(0, 0):1, (0, 1):2, (0, 2):3, (1, 0):4, (1, 1):5,\
             (1, 2):6, (2, 0):7, (2, 1):8, (2, 2):9}
        return  d[(a[0], a[1])]
    elif type(a) is int: # se a for uma posicao
        d = {1:(0, 0), 2:(0, 1), 3:(0, 2), 4:(1, 0), 5:(1, 1),\
             6:(1, 2), 7:(2, 0), 8:(2, 1), 9:(2, 2)}
        return d[a]
    
def eh_posicao_livre(tab, posicao):
    #tabuleiro x posicao -> bool
    '''recebe um taubleiro tab uma posicao posicao e devolve True se a posicao
    for livre ou False caso contrario'''
    if eh_tabuleiro(tab) and eh_posicao(posicao):
        a, b = converter_pos_coord(posicao)
        if tab[a][b] == 0: return True
        return False
    raise ValueError('eh_posicao_livre: algum dos argumentos e invalido')

def obter_posicoes_livres(tab):
    #tablueiro -> tabuleiro
    '''recebe um tabulerio tab e devolve um tuplo com as posicoes livres do 
    tabuleiro'''
    if eh_tabuleiro(tab):
        livre = []
        for pos in range (1, 10):
            if eh_posicao_livre(tab, pos):
                livre += [pos]
        return tuple(livre)
    raise ValueError ('obter_posicoes_livres: o argumento e invalido')

def jogador_ganhador(tab):
    #tabuleiro -> inteiro
    '''recebe um tabuleiro tab e devolve um inteiro igual ao numero do jogador
    vencedor ou 0 cajo nao haja vencedor'''
    if eh_tabuleiro(tab):
        for i in range(len(tab)):
            if (tab[i][0] == tab[i][1] == tab[i][2]): #verifica linhas
                return tab[i][0]
            elif (tab[0][i] == tab[1][i] == tab[2][i]): #verifica colunas
                return tab[0][i]
        if tab[0][0] == tab[1][1] == tab[2][2] \
        or tab[2][0] == tab[1][1] == tab[0][2]: # verifica diagonais
            return tab[1][1]    
        return 0        
    raise ValueError ('jogador_ganhador: o argumento e invalido')

def marcar_posicao(tab, jogad, pos):
    #tabuleiro x jogador x posicao -> tabuleiro
    '''recebe um tabuleiro tab um jogador jogador e uma posicao posicao devolve 
    um tabuleiro tab_alterado marcado com pecao do jogador na posicao'''
    #Verificar validade de tab e de pos
    if eh_tabuleiro(tab) and eh_posicao(pos):
        #Veficar se pos esta livre e validade de jogad
        if eh_posicao_livre(tab, pos) and eh_jogador(jogad):
            coordenadas = converter_pos_coord(pos)
            tuplo = tab[coordenadas[0]]
            tuplo_alterado = tuple(tuplo[i] if i != coordenadas[1] \
            else jogad for i in range(len(tuplo)))
            tab_alterado = tuple(tab[i] if i != coordenadas[0] \
            else tuplo_alterado for i in range(len(tab)))
            return tab_alterado
    raise ValueError ('marcar_posicao: algum dos argumentos e invalido')

def escolher_posicao_manual(tab):
    #tabuleiro -> posicao
    '''recebe um tabuleiro tab e devolve uma posicao introduziada pelo jogador
    caso esta esteja livre'''    
    if eh_tabuleiro(tab):
        posicao = int(input('Turno do jogador. Escolha uma posicao livre: '))
        if eh_posicao(posicao):
            if eh_posicao_livre(tab, posicao):
                return posicao
        raise ValueError ('escolher_posicao_manual: a posicao introduzida e invalida')
    raise ValueError ('escolher_posicao_manual: o argumento e invalido')

def centro(tab, jogad): #jogador e argumento por qustoes de simplificacao
    #tabuleiro x jogador -> posicao
    '''recebe um tabuleiro tab e um jogador jogad e devolve a posicao do centro
    do tabuleiro ou string vazia se esta estiver ocupada'''    
    if eh_posicao_livre(tab, 5):
        return 5
    return ''

def canto_oposto(tab, jogad):
    #tabuleiro x jogador -> posicao
    '''recebe um tabuleiro tab e um jogador jogad e devolve uma posicao de um 
    canto do tabuleiro oposto a um canto ocupado pelo adversario ou string vazia
    caso uma posicao nessas condicoes nao exista'''
    for cantos in [(0, 0), (0, 2), (2, 0), (2, 2)]:
        if tab[cantos[0]][cantos[1]] == -jogad:
            canto_oposto = converter_pos_coord((2 - cantos[0], 2 - cantos[1]))
            if eh_posicao_livre(tab, canto_oposto):
                return canto_oposto
    return ''

def posicao_exterior_vazia(tab, chave):
    #tabuleiro x chave-> posicao
    '''recebe um tabuleiro tab e uma string chave e devolve uma e devolve uma 
    posicao vazia do tabuleiro correspondente a chave ou string vazia caso nao
    exista uma posicao nessas condicoes''' 
    posicoes = {'cantos' : [1, 3, 7, 9], 'laterais' : [2, 4, 6, 8]}
    for posicao in posicoes[chave]:
        if eh_posicao_livre(tab, posicao): 
            return posicao 
    return ''

def canto_vazio(tab, jogad): #jogador e argumento para simplificacao
    #tabuleiro x jogador -> posicao
    '''recebe um tabuleiro tab e um jogador jogad e devolve a posicao de um 
    canto vazio do tabuleiro ou string vazia caso nao exista'''
    return posicao_exterior_vazia(tab, 'cantos')

def lateral_vazio(tab, jogad): #jogador e argumento para simplificacao
    #tabuleiro x jogador -> posicao
    '''recebe um tabuleiro tab e um jogador jogad e retorna a posicao de uma 
    lateral vazia do tabuleiro ou string vazia caso nao exista'''    
    return posicao_exterior_vazia(tab, 'laterais')

def total_ocurrencias(linha, x):
    #tuplo x inteiro -> inteiro
    '''recebe um tuplo linha e um inteiro x um inteiro total igual ao numero de
    ocorrencias de x no tuplo'''
    total = 0
    for e in linha:
        if e == x: total += 1
    return total

def verifica_elementos(linha, jogad, a, b):
    #tuplo x jogador x inteirox inteiro -> bool
    '''recebe um tuplo linha, jogador jogad, inteiro a e um inteiro b devolve 
    True se o tuplo tem a vezes o elemento x e b posicoes livres ou False caso
    contrario'''
    if total_ocurrencias(linha, jogad) == a and total_ocurrencias(linha, 0) == b:
        return True
    return False

def obter_tuplo(tab, i, tipo):
    #tabuleiro x numero de linha x tipo de linha -> tuplo
    '''recebe um tabuleiro tab um inteiro i, numero da linha/coluna/diagonal a
    obter e um inteiro tipo e devolve (i + 1) esima linha/coluna e i esima
    diagonal'''
    linha  = ()
    if tipo == 1: 
        linha = obter_linha(tab, i + 1)
    elif tipo == 2: 
        linha = obter_coluna(tab, i + 1)
    elif tipo == 3 and i != 0: #nao existe diagonal 0
        linha = obter_diagonal(tab, i)    
    return linha

def verifica_tabuleiro(tab, jogad, a, b):
    #tabuleiro x jogador x inteiro x inteiro -> tuplo de posicoes
    '''recebe um tabuleiro tab um jogador jogad e dois inteiros um a numero de
    elementos jogad que tem de existir numa linha e um b numero de posicoes
    livres que tem de existir numa linha e devolve tuplo com as posicoes livres 
    linhas/colunas/diagonais com a elementos jogad e b posicoes livres'''
    def verificar_tuplo(tab, jogad, i, tipo, a, b):  
    #tabuleiro x jogador x tipo de linha x numero de linha x inteiro 
    # x inteiro -> lista posicoes
        '''recebe um tabuleiro tab um jogador jogad um tipo de linha tipo um 
        inteiro i que em conjunto com tipo determinam o tuplo a estudar e os 
        inteiros a e b com a funcao de verifica_tabuleiro e devolve um tuplo com
        as posicoes livres da linha/coluna/diagonal se esta tiver a elementos x 
        e b posicoes livres ou tuplo vazio caso contrario'''
        posicoes = []
        linha = obter_tuplo(tab, i, tipo) # obtem o tuplo a estudar
        #verifica se o tuplo cumpre as condicoes de elegibilidade para recolha
        if verifica_elementos(linha, jogad, a, b): 
            for j in range(len(tab)): # recolhe posicoes livres do tuplo
                if tipo == 1 and tab[i][j] == 0: 
                    posicoes += [(i, j)] # linhas
                elif tipo == 2 and tab[j][i] == 0: 
                    posicoes += [(j, i)] # colunas
                elif tipo == 3 and i == 1 and tab[j][j] == 0:
                    posicoes += [(j, j)]  #diagonal 1 -> (j, j)
                elif tipo == 3 and i == 2 and tab[2 - j][j] == 0: 
                    posicoes += [(2 - j, j)] #diagonal 2 -> (2 - j, j)
        return [converter_pos_coord(elemento) for elemento in posicoes]
    
    posicoes_vitoria = []
    for tipo in [1, 2, 3]: #itera entre estudo de linhas, colunas e diagonais
        for i in range(len(tab)): #tabuleiro quadrado no. linhas e colunas igual
            if tipo == 3 and i == 0: continue #nao existe diagonal 0 
            posicoes_vitoria += verificar_tuplo(tab, jogad, i, tipo, a, b)
    return tuple(sorted(set(posicoes_vitoria)))

def vitoria(tab, jogad):
    #tabuleiro x jogador -> posicao
    '''recebe um tabuleiro tab e jogador jogad devolve uma posicao de vitoria
    ou string vazia se nao existir nenhuma'''    
    jogada = verifica_tabuleiro(tab, jogad, 2, 1) 
    return jogada[0] if len(jogada) > 0 else ''

def bloqueio(tab, jogad):
    #tabuleiro x jogador -> posicao
    '''recebe um tabuleiro tab e um jogador jogad devolve uma posicao de vitoria
    do adversario string vazia se nao existir nenhuma'''
    jogada = verifica_tabuleiro(tab, -jogad, 2, 1)
    return jogada[0] if len(jogada) > 0 else ''

def procura_bifurcacoes(tab, jogad):
    #tabuleiro x jogador -> tuplo de posicoes
    '''recebe um tabuleiro tab e um jogador jogad e devolve um tuplo com as 
    posicoes que permitem ao jogador bifrucar (gerar 2 posicos de vitoria)
    ordenadas ascendentemente'''
    intersecoes = []
    for tipo in [1, 2]: #tipo 1 -> linhas | tipo 2 -> colunas
        for i in range(len(tab)):
            tuplo = obter_tuplo(tab, i, tipo)
            #verifica se o tuplo pode bifurcar (1 elem jogad e 2 elementos 0)
            if verifica_elementos(tuplo, jogad, 1, 2): 
                for j in range(len(tuplo)):
                #para tipo = 1 verificam-se bifurcacoes em linhas + colunas e 
                #linhas + diagonais, para tipo = 2 apenas colunas + diagonais 
                #posicao de bifurcacao tem de ser posicao livre
                    if (tipo == 1 and tab[i][j] == 0) or \
                       (tipo == 2 and tab[j][i] == 0):
                        #tuplo e linha e a posicao e livre -> verificar coluna
                        if tipo == 1 and verifica_elementos(\
                            obter_coluna(tab, j + 1), jogad, 1, 2): 
                            intersecoes += [(i, j)] #adiciona posicao ao tuplo
                        #se i = j a posicao (i, j) pertence a diagonal 1
                        elif i == j and verifica_elementos(\
                        obter_diagonal(tab, 1), jogad, 1, 2): 
                            intersecoes += [(i, j)] 
                        #tuplo e linha e 2 - i = j ou tuplo e coluna e 2 - j = i
                        #posicao (i, j) ou (j, i) esta na diagonal 2, respetiv.
                        elif ((2 - i == j and tipo == 1) or (2 - j == i and \
                        tipo == 2)) and verifica_elementos(\
                        obter_diagonal(tab, 2), jogad, 1, 2):
                            
                            if tipo == 1: intersecoes += [(i, j)]
                            elif tipo == 2: intersecoes += [(j, i)] 
                            
    if eh_posicao_livre(tab, 5):  #verificar bifurcacao diagonal + diagonal
        if verifica_elementos(obter_diagonal(tab, 1), jogad, 1, 2) \
           and verifica_elementos(obter_diagonal(tab, 2), jogad, 1, 2): 
            intersecoes += [(1, 1)]
            
    posicoes_intersecao = [converter_pos_coord(elem) for elem in intersecoes]
    return tuple(sorted(set(posicoes_intersecao))) 

def bifurcacao(tab, jogad):
    #tabuleiro x jogador -> posicao
    '''recebe um tabuleiro tab e um jogador jogad e devolve uma posicao que 
    permite ao jogador bifurcar caso contrario devolve string vazia'''
    jogada = procura_bifurcacoes(tab, jogad)
    return jogada[0] if len(jogada) > 0 else ''
     

def forca_defesa(tab, jogad):
    # tabuleiro x jogador -> posicao
    '''recebe um tabuleiro tab e um jogador jogad e devolve uma posicao jogada
    que forca defender sem que esta gere uma bifurcacao ou string vazia se essa
    nao existir'''
    #procurar todas as posicoes livres em linhas/colunas/diagonais 
    #com 1 peca do jogador e 2 posicoes livres
    jogadas_candidatas = verifica_tabuleiro(tab, jogad, 1, 2)
    #verificar se defesa a jogada em cada posicao gera bifurcacao
    for jogada in jogadas_candidatas:
        tab_candidato = marcar_posicao(tab, jogad, jogada)
        tab_defesa = marcar_posicao(tab_candidato, -jogad, bloqueio(tab_candidato, -jogad))
        jogadas_vitoria_adv = verifica_tabuleiro(tab_defesa, -jogad, 2, 1)
        if len(jogadas_vitoria_adv) > 1: #posicao de defesa bifurca
            continue 
        else: #posicao de defesa nao bifurca -> retorna posicao 
            return jogada
    return ''
        
def bloqueio_bifurcacao(tab, jogad):
    #tabuleiro x jogador -> posicao
    '''recebe um tabuleiro e um jogador e devolve uma posicao que impede o
    adversario de bifurcar'''
    intersecoes_adversario = procura_bifurcacoes(tab, -jogad)
    if len(intersecoes_adversario) == 0: 
        return ''
    elif len(intersecoes_adversario) == 1:    
        return intersecoes_adversario[0]
    else: 
        return forca_defesa(tab, jogad)

def escolher_acoes(estrategia):  
    #estrategia -> lista
    '''recebe uma estrategia e retorna uma lista com os indices das acoes 
    ordenadas que lhe correspondem'''
    if estrategia == 'basico': return [5, 7, 8]
    if estrategia == 'normal': return [1, 2, 5, 6, 7, 8]
    else: return [1, 2, 3, 4, 5, 6, 7, 8, 9]   

def acoes(i):
    #inteiro -> funcao
    '''recebe um inteiro e retorna a funcao que lhe corresponde'''
    d = {1 : vitoria, 2 : bloqueio, 3 : bifurcacao, 4 : bloqueio_bifurcacao, 
         5 : centro, 6 : canto_oposto, 7 : canto_vazio, 8 : lateral_vazio}
    return d[i]  

def escolher_posicao_auto(tab, jogad, estrategia):
    #tabuleiro x jogador x estrategia -> posicao
    '''recebe um tabuleiro tab um jogador jogad e uma estrategia estrategia do 
    computador e retorna a posicao de jogada do computador'''
    if eh_tabuleiro(tab) and eh_estrategia(estrategia) and eh_jogador(jogad):
        chave_acoes = escolher_acoes(estrategia)
        for chave in chave_acoes:
            acao = acoes(chave)
            jogada = acao(tab, jogad)
            if jogada != '': 
                return jogada
    #se nao hanenhuma jogada disponivel a funcao nao retorna nada e levanta erro
    raise ValueError ('escolher_posicao_auto: algum dos argumentos e invalido')

def eh_marca_valida(marca):
    #universal -> bool
    '''recebe um universal marca e devolve True se for marca de jogador e False 
    caso contrario'''
    if type(marca) is str:
        if marca == 'X' or marca == 'O': 
            return True
    return False

def eh_jogador(jogad):
    #universal -> bool
    '''recebe universal jogad devolve True se e jogador caso contrario False'''
    if type(jogad) is int and (jogad == 1 or jogad == -1):
        return True
    return False

def eh_estrategia(estrategia):
    #universal -> bool
    '''recebe um universal estrategia devolve True se for estrategia 
    e False caso contrario'''
    if type(estrategia) is str:
        if estrategia == 'perfeito' or estrategia == 'normal' \
           or estrategia == 'basico': 
            return True
    return False

def estado_do_jogo(tab):
    #tabuleiro -> estado do jogo
    '''recebe um tabuleiro tab e devolve uma string vazia se o resultado e 
    desconhecido, igual a marca do jogador vencedor ou EMPATE se ha empate'''
    if jogador_ganhador(tab) != 0:
        return 'X' if jogador_ganhador(tab) == 1 else 'O' #devolve vencedor
    elif obter_posicoes_livres(tab) == ():
        return 'EMPATE'
    return '' #devolve strig vazia se o jogo estiver em progresso
    
def loop_jogo(tab, jogad, estrategia):
    #tabuleiro x jogador x estrategia -> resultado
    '''recebe um tabuleiro tab um jogador jogad e uma estrategia estrategiae e
    devolve uma string, igual a marca do vencedor ou EMPATE no caso de empate'''
    computador = -jogad
    while True:
        #Turno do jogador
        tab = marcar_posicao(tab, jogad, escolher_posicao_manual(tab))
        print(tabuleiro_str(tab))
        if estado_do_jogo(tab) != '': break
        #Turno do computador
        print('Turno do computador (' + estrategia +'):')
        tab = marcar_posicao(tab, computador, \
        escolher_posicao_auto(tab, computador, estrategia))
        print(tabuleiro_str(tab))
        if estado_do_jogo(tab) != '': break
    return estado_do_jogo(tab)

def jogo_do_galo(marca_jogador, estrategia_computador):
    #marca x estrategia -> resultado
    '''recebe a marca do jogador marca_jogador e a estrategia do computador 
    estrategia e devolve uma string resultado com a marca do vencedor ou 
    EMPATE no caso de empate'''    
    if eh_marca_valida(marca_jogador) and eh_estrategia(estrategia_computador):
        print('Bem-vindo ao JOGO DO GALO.')
        print('O jogador joga com \'{0}\'.'.format(marca_jogador))
        jogador = 1 if marca_jogador == 'X' else -1
        tab = ((0,0,0),(0,0,0),(0,0,0))
        if jogador == -1: #Caso em que o computador comeca
            print('Turno do computador (' + estrategia_computador +'):')
            tab = marcar_posicao(tab, 1, \
            escolher_posicao_auto(tab, -jogador, estrategia_computador))
            print(tabuleiro_str(tab))
        resultado = loop_jogo(tab, jogador, estrategia_computador) #invoca loop
        return resultado
    raise ValueError ('jogo_do_galo: algum dos argumentos e invalido')