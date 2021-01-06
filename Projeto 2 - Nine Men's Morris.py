# Alexandre Faisca Coelho ist1100120
LINHAS, COLUNAS = ['1', '2', '3'], ['a', 'b', 'c']


# TAD posicao
# Representacao interna: tuplo de dois elementos -> 1st == coluna 2nd == linha
# Operacoes basicas
# cria_posicao: str x str -> posicao
# cria_copia_posicao: posicao -> posicao
# obter_pos_c: posicao -> str
# obter_pos_l: posicao -> str
# eh_posicao: universal -> bool
# posicao_iguais: posicao x posicao -> bool
# posicao_para_str: posicao -> str
def cria_posicao(c, l):
    # str x str -> posicao
    '''recebe duas cadeias de caracteres correspondentes a coluna c e a linha l
    de uma posicao e devolve a posicao correspondente'''
    if c in COLUNAS and l in LINHAS:  # verificar validade dos argumentos
        return (c, l)  # posicao representada internamente como tuplo
    else:
        raise ValueError('cria_posicao: argumentos invalidos')


def cria_copia_posicao(p):
    # posicao -> posicao
    '''recebe uma posicao e devolve um acopia nova da posicao'''
    return cria_posicao(obter_pos_c(p), obter_pos_l(p))


def obter_pos_c(p):
    # posicao -> str
    '''recebe uma posicao p e devolve a componente coluna c'''
    return p[0]  # coluna armazenada como primeiro elemento do tuplo


def obter_pos_l(p):
    # posicao -> str
    '''recebe uma posicao p e devolve a componente linha l'''
    return p[1]  # linha armazenada como segundo elemento do tuplo


def eh_posicao(arg):
    # universal -> booleano
    '''devolve True se o argumento for uma posicao e False caso contrario'''
    return type(arg) is tuple and len(arg) == 2 and arg[0] in COLUNAS \
           and arg[1] in LINHAS


def posicoes_iguais(p1, p2):
    # posicao x posicao -> booleano
    '''recebe duas posicoes, p1 e p2, e devolve True se p1 e p2 sao posicoes e
    sao iguais'''
    return eh_posicao(p1) and eh_posicao(p2) and obter_pos_c(p1) == \
           obter_pos_c(p2) and obter_pos_l(p1) == obter_pos_l(p2)


def posicao_para_str(p):
    # posicao -> str
    '''recebe uma posicao p e devolve uma cadeia caracteres que corresponde a
    concatenar a coluna c e a linha l da posicao p'''
    return obter_pos_c(p) + obter_pos_l(p)  # obter e concatenar linha e coluna


def obter_posicoes_adjacentes(p):
    # posicao -> tuplo de posicoes
    '''recebe uma posicao p e devolve um tuplo com as posicoes adjacentes a 
    posicao p de acordo com a ordem de leitura do tabuleiro'''
    posicoes = ()
    # obter linha e coluna (l / c) da posicao p
    l = obter_pos_l(p)  # linha
    c = obter_pos_c(p)  # coluna
    # obter linhas e colunas adjacentes a p
    # caracteres que sao linhas / colunas e cuja diferenca da representacao ASCII
    # com a representacao ASCII de l / c, em modulo, e menor ou igual a 1
    l_adjacentes = [v for v in [chr(ord(l) - 1), l, chr(ord(l) + 1)] if v in LINHAS]
    c_adjacentes = [v for v in [chr(ord(c) - 1), c, chr(ord(c) + 1)] if v in COLUNAS]
    for linha in l_adjacentes:  # iterar pelas linhas adjacentes
        for coluna in c_adjacentes:  # iterar pelas colunas adjacentes
            candidato = cria_posicao(coluna, linha)
            # verificar se satisfaz condicoes de adjacencia
            if (not posicoes_iguais(p, candidato)) and \
                    (linha == l or coluna == c or ((c == 'a' or c == 'c') and (l == '1' \
                                                                               or l == '3')) or (
                             c == 'b' and l == '2')):
                posicoes = posicoes + (candidato,)
    return posicoes


# Estabelecimento de correspondencia entre as posicoes do tabuleiro e os inteiros
# 0 a 8 para facilitar e tornar intuitiva a iteracao das posicoes num tabuleiro
def posicao_para_inteiro(p):
    # posicao -> inteiro
    '''recebe uma posicao e devolve o inteiro de 0 a 8 corespondente a posicao
    considerando uma ordem de leitura do tabuleiro esq-dir, cima-baixo'''
    return (ord(obter_pos_c(p)) - 97) + ((int(obter_pos_l(p)) - 1) * 3)


def inteiro_para_posicao(n):
    # inteiro -> posicao
    '''recebe um inteiro de 0 a 8 e devolve a posicao correspondente ao inteiro
    considerando uma ordem de leitura do tabuleiro esq-dir, cima-baixo'''
    return cria_posicao(chr((n % 3) + 97), str((n // 3) + 1))


def posicao_no_tuplo(p, t):  # substituicao da operacao posicao in tuplo
    # posicao x tuplo -> bool
    '''recebe uma posicao e um tuplo e devolve True se a posicao e elemento do
    tuplo e False caso contrario'''
    return [posicoes_iguais(p, pos) for pos in t].count(True) != 0


# TAD peca
# Representacao interna: tuplo de um elemento ((-1,), (1,) ou (0,))
# Operacoes basicas:
# cria_peca: str -> peca
# cria_copia_peca: peca -> peca
# eh_peca: universal -> bool
# pecas_iguais: peca x peca -> bool
# peca_para_str: peca -> str
def cria_peca(s):
    # str -> peca
    '''recebe uma cadeia de caracteres identificadora do jogador, 'X', 'O'
    ou ' ' no caso de peca livre e devolve a peca correspondente'''
    if s in ['X', 'O', ' ']:  # verificar validade do argumento
        return (1,) if s == 'X' else ((-1,) if s == 'O' else (0,))  # criar peca
    else:
        raise ValueError('cria_peca: argumento invalido')


def cria_copia_peca(j):
    # peca -> peca
    '''recebe uma peca e devolve uma copia nova da peca'''
    return (j[0],)


def eh_peca(arg):
    # universal -> booleano
    '''devolve True se o argumento for peca e False caso contrario'''
    return type(arg) is tuple and len(arg) == 1 and arg[0] in [-1, 0, 1]


def pecas_iguais(j1, j2):
    # peca x peca -> booleano
    '''recebe duas pecas j1 e j2 devolve True apenas se j1 e j2 sao pecas 
    iguais'''
    return eh_peca(j1) and eh_peca(j2) and j1[0] == j2[0]


def peca_para_str(j):
    # peca -> str
    '''devolve a cadeia de caracteres que representa o jogador dono da peca'''
    return '[ ]' if j[0] == 0 else \
        '[X]' if j[0] == 1 else '[O]'


# Estabelecimento de correspondencia entre as pecas de jogador e os inteiros -1 a
# 1 para facilitar transicao entre pecas e modo como sao guardadas no tabuleiro
def peca_para_inteiro(j):
    # peca -> n
    '''devolve um inteiro valor 1, -1 ou 0 dependendo se a peca e do jogador 
    'X', 'O', ou livre, respetivamente'''
    return 1 if peca_para_str(j) == '[X]' else \
        -1 if peca_para_str(j) == '[O]' else 0


def inteiro_para_peca(n):
    # n -> peca
    '''recebe um inteiro n valor 1, -1 ou 0 e devolve a peca do jogador
    do jogador, 'X', 'O', ou livre respetivamente'''
    return cria_peca('X') if n == 1 else \
        (cria_peca('O') if n == -1 else cria_peca(' '))


def peca_no_tuplo(j,t,n):
    #peca x tuplo x inteiro -> bool
    '''recebe uma peca um tuplo e um inteiro n e devolve True se a peca surgir no
    tuplo exatamente n vezes e False caso contrario'''
    if [pecas_iguais(j, peca) for peca in t].count(True) == n:
        return True
    else: return False


# TAD tabuleiro
# Representacao interna: lista de nove elementos (1, 0 ou -1) representando pecas
# Operacoes basicas:
# cria_tabuleiro: {} -> tabuleiro
# cria_copia_tabuleiro: tabuleiro -> tabuleiro
# obter_peca: tabuleiro x posicao -> peca
# obter_vetor: tabuleiro x str -> tuplo de pecas
# coloca_peca: tabuleiro x peca x posicao -> tabuleiro
# remove_peca: tabuleiro x posicao -> tabuleiro
# move_peca: tabuleiro x posicao x posicao -> tabuleiro
# eh_tabuleiro: universal -> bool
# eh_posicao_livre -> tabuleiro x posicao -> bool
# tabuleiros_iguais -> tabuleiro x tabuleiro -> bool
# tabuleiro_para_str: tabuleiro -> str
# tuplo_para_tabuleiro: tuplo -> tabuleiro
def cria_tabuleiro():
    # {} -> tabuleiro
    '''devolve um tabuleiro de jogo do moinho de 3x3 sem posicoes ocupadas'''
    # tabuleiro representado internamente como lista 9 elementos (posicoes 0 a 8)
    return [0, 0, 0, 0, 0, 0, 0, 0, 0]


def cria_copia_tabuleiro(t):
    # tabuleiro -> tabuleiro
    '''recebe um tabuleiro t e devolve uma copia nova do tabuleiro'''
    if eh_tabuleiro(t):  # verificar validade do argumento
        return [e for e in t]  # construir copia do tabuleiro e devolve-la


def obter_peca(t, p):
    # tabuleiro x posicao -> peca
    '''recebe um tabuleiro t e uma posicao p e devolve a peca na posicao p do 
    tabuleiro, se a posicao nao estiver ocupada devolve uma peca livre'''
    return inteiro_para_peca(t[posicao_para_inteiro(p)])


def obter_vetor(t, s):
    # tabuleiro x str -> tuplo de pecas
    '''recebe um tabuleiro e uma cadeia de caracteres escpecificando uma linha
    ou coluna devolve tuplo com todas as pecas dessa linha ou coluna'''
    if s in LINHAS:
        return tuple(inteiro_para_peca(t[(ord(s) - 49) * 3 + i]) for i in range(3))
    elif s in COLUNAS:
        return tuple(inteiro_para_peca(t[3 * i + (ord(s) - 97)]) for i in range(3))


def coloca_peca(t, j, p):
    # tabuleiro x peca x posicao -> tabuleiro
    '''recebe um tabuleiro t uma peca j e  uma posicao p e modifica
    destrutivamente o tabuleiro t colocando a peca j na posicao p
    e devolve o proprio tabuleiro t'''
    t[posicao_para_inteiro(p)] = peca_para_inteiro(j)  # colocar peca
    return t  # devolver tabuleiro modificado


def remove_peca(t, p):
    # tabuleiro x posicao -> tabuleiro
    '''recebe um tabuleiro t e uma posicao p e modifica destrutivamente o
    removendo a peca da posicao p e devolve o proprio tabuleiro t'''
    peca_livre = cria_peca(' ')  # criar peca livre
    return coloca_peca(t, peca_livre, p)  # colocar peca livre na posicao p


def move_peca(t, p1, p2):
    # tabuleiro x posicao x posicao -> tabuleiro
    '''recebe um tabuleiro t e duas posicoes p1 e p2 e modifica destrutivamente
    o tabuleiro t movendo a peca que se encontra em p1 para a posicao p2 e
    devolve o proprio tabuleiro t'''
    j = obter_peca(t, p1)  # obter peca a mover (peca na posicao p1)
    return coloca_peca(remove_peca(t, p1), j, p2)  # mover a peca para posicao p2


def eh_tabuleiro(arg):
    # universal -> booleano
    '''devolve True caso o seu argumento seja um TAD tabuleiro (valido) e False
    caso contrario, um tabuleiro valido pode ter um maximo de tres pecas de cada
    jogador, nao pode conter mais de 1 peca mais de um jogador que do contrario,
    e apenas pode haver um ganhador em simultaneo'''

    def numero_ganhador_legal():
        # universal -> boolean
        '''recebe um universal (que tem formato de tabuleiro) devolve True se 
        houver um ou nenhum vencedor e False caso contrario'''
        cont = 0
        if len(obter_posicoes_livres(arg)) == 3:  # verificar se ha 6 pecas em jogo
            for linha in LINHAS + COLUNAS:  # percorrer todas linhas do tabuleiro
                vetor = obter_vetor(arg, linha)
                if peca_no_tuplo(vetor[0], vetor, 3):
                    cont = cont + 1  # aumentar contagem
        if cont < 3:
            return True  # contagem menor que tres -> numero legal
        else:
            return False  # se contagem e tres ha dois vencedores -> invalido

    return (type(arg) is list) and len(arg) == 9 and (arg.count(0) + arg.count(1) \
                                                      + arg.count(-1) == 9) and arg.count(1) < 4 and arg.count(
        -1) < 4 and \
           abs(arg.count(1) - arg.count(-1)) <= 1 and numero_ganhador_legal(arg)


def eh_posicao_livre(t, p):
    # tabuleiro x posicao -> booleano
    '''recebe um tabuleiro t e uma posicao p, devolve True se a posicao p do 
    tabuleiro t corresponder a posicao livre e False caso contrario'''
    return t[posicao_para_inteiro(p)] == 0  # peca livre e representada por 0


def tabuleiros_iguais(t1, t2):
    # tabuleiro x tabuleiro -> booleano
    '''recebe dois tabuleiros t1 e t2, devolve True se forem ambos tabuleiros e
    forem iguais e False caso contrario'''
    # criar uma lista de valores booleanos, com o valor de t1 == t2 para cada
    # elemento dos tabuleiros, e averiguar quantos dos elementos sao 'True'
    return eh_tabuleiro(t1) and eh_tabuleiro(t2) and \
           list(t1[i] == t2[i] for i in range(9)).count(True) == 9


def tabuleiro_para_str(t):
    # tabuleiro -> str
    '''recebe um tabuleiro t e devolve a cadeia de caracteres que representa o
    tabuleiro'''
    string = '   a   b   c\n'  # primeira linha do tabuleiro constante durante jogo
    separador = ['   | \\ | / |\n', '   | / | \\ |\n']
    for i in range(3):
        # concatenar linha com pecas. Forma das linhas constante durante o jogo:
        string = string + '{0:} {1:}-{2:}-{3:}'. \
            format(i + 1, peca_para_str(inteiro_para_peca(t[i * 3])), \
                   peca_para_str(inteiro_para_peca(t[i * 3 + 1])), \
                   peca_para_str(inteiro_para_peca(t[i * 3 + 2])))
        if i != 2:  # concatenar caracter EOL e separador entre linhas com pecas
            string = string + '\n' + separador[i]
    return string  # devolver string com representacao externa do tabuleiro


def tuplo_para_tabuleiro(t):
    # tuplo -> tabuleiro
    '''recebe um tuplo t com 3 tuplos, cada um deles contendo inteiros iguais a 
    1, -1 ou 0 e devolve o tabuleiro por este representado'''

    def tuplo_para_tabuleiro_aux(tab, t):
        if t == ():  # caso terminal
            return tab  # devolver tabuleiro
        elif type(t[0]) is tuple:  # alisar primeiro elemento se este for tuplo
            return tuplo_para_tabuleiro_aux(tab, t[0] + t[1:])
        else:  # se primeiro elemento e inteiro juntar ao tabuleiro
            return tuplo_para_tabuleiro_aux(tab + [t[0]], t[1:])

    return tuplo_para_tabuleiro_aux([], t)


def obter_ganhador(t):
    # tabuleiro -> peca
    '''recebe um tabuleiro t e devolve uma peca do jogador ganhador, ou peca
    livre se nao existir ganhador'''
    for linha in LINHAS + COLUNAS:  # iterar todas as linhas do tabuleiro
        tuplo = obter_vetor(t, linha)  # obter tuplo que representa cada linha
        if peca_no_tuplo(cria_peca('X'), tuplo, 3) or peca_no_tuplo(cria_peca(\
                'O'), tuplo, 3): # verificar se tuplo possui tres pecas iguais
            return tuplo[0]  # devolver peca na primeira posicao do tuplo
    return cria_peca(' ')  # nao ha vencedor -> devolver peca livre


def obter_posicoes_jogador(t, j):
    # tabuleiro x peca -> tuplo de posicoes
    '''recebe um tabuleiro t e uma peca j correspondente ao jogador e devolve um
    tuplo com as posicoes do tabuleiro t ocupadas pelo jogador ordenadas segundo
    a ordem de leitura do tabuleiro'''
    posicoes_peca = ()
    # iterar pelas posicoes da esq para dir e de cima para baixo verificando peca
    for i in range(9):
        posicao = inteiro_para_posicao(i)  # obter posicao
        if pecas_iguais(obter_peca(t, posicao), j):  # verificar se e peca jogador
            posicoes_peca = posicoes_peca + (posicao,)  # se sim, guardar posicao
    return posicoes_peca  # devolver tuplo contendo posicoes do jogador ordenadas


def obter_posicoes_livres(t):
    # tabuleiro -> tuplo de posicoes
    '''recebe um tabuleiro t e devolve um tuplo com as posicoes nao ocupadas
    pelas pecas de qualquer dos jogadores na ordem de leitura do tabuleiro'''
    # equivalente a obter posicoes ocupadas pelo jogador que joga peca livre
    return obter_posicoes_jogador(t, cria_peca(' '))


def existe_movimento_disponivel(t, j):
    # tabuleiro x peca -> boolean
    '''recebe um tabuleiro e uma peca e devolve True se o jogador representado
    pela peca tem movimentos disponiveis e False caso contrario'''
    pos_jogador = obter_posicoes_jogador(t, j)  # obter posicoes do jogador
    pos_livres = obter_posicoes_livres(t)  # obter posicoes livres
    for posicao in pos_jogador:  # obter posicoes adjacentes a cada pos jogador
        pos_adjacentes = obter_posicoes_adjacentes(posicao)
        for adjacente in pos_adjacentes:  # verificar se adjacente e posicao livre
            if posicao_no_tuplo(adjacente, pos_livres):
                return True  # devolver True se houver uma posicao adjacente livre
    else:
        return False  # devolver False se nao ha posicoes elegiveis como destino


def obter_movimento_manual(t, j):
    # tabuleiro x peca -> tuplo de posicoes
    '''recebe um tabuleiro t e uma peca j e devolve um tuplo com uma ou duas
    posicoes introduzidas manualmente pelo jogador, dependendo de o jogo estar 
    na fase de colocacao ou de movimento, respetivamente'''
    mensagem = ('Turno do jogador. Escolha uma posicao: ', \
                'Turno do jogador. Escolha um movimento: ')
    pos_livres = obter_posicoes_livres(t)  # obter posicoes livres tabuleiro
    x = 0  # x == 0 -> fase de colocacao
    if len(pos_livres) == 3: x = 1  # x == 1 -> fase de movimentacao
    jog = input(mensagem[x])  # obter escolha do jogador, passar a verificacao
    if jog[0] in COLUNAS and jog[1] in LINHAS and ((x == 0 and len(jog) == 2) or \
                                                   (len(jog) == 4 and jog[2] in COLUNAS and jog[3] in LINHAS)):
        p = (cria_posicao(jog[0], jog[1]),) if x == 0 else (cria_posicao(jog[2], \
                                                                         jog[3]), cria_posicao(jog[0], jog[
            1]))  # converter string para tuplo de pos
        # verificar se posicoes escolhidas sao validas
        pos_jogador = obter_posicoes_jogador(t, j)  # obter pos com peca jogador
        if posicao_no_tuplo(p[0], pos_livres) and (x == 0 or posicao_no_tuplo( \
                p[1], pos_jogador) and posicao_no_tuplo(p[0], \
                                                        obter_posicoes_adjacentes(p[1]))):
            return p if x == 0 else (p[1], p[0])  # repor ordem se x == 1
        # verificar se se trata do caso em que nao ha movimentos disponiveis
        if x == 1 and posicoes_iguais(p[0], p[1]) and \
                (not existe_movimento_disponivel(t, j)):
            return p  # devolver tuplo com duas posicoes iguais
    # se escolha e invalida gerar mensagem de erro
    raise ValueError('obter_movimento_manual: escolha invalida')


def minimax(t, j, profundidade, seq_movimentos):  # com base no pseudocodigo fornecido
    # tabuleiro x peca x inteiro x tuplo -> posicao 
    '''recebe um tabuleiro uma peca um inteiro indicando a profundidade de 
    recursao e um tuplo e devolve um tuplo com a concatenacao do tuplo recebido
    e a sequencia de movimentos que favorece o jogador e com o valor do
    tabuleiro obtido executando essa sequencia de movimentos'''
    melhor_seq_movimentos = ()  # atribuir valor nulo a melhor sequencia
    if (not pecas_iguais(obter_ganhador(t), cria_peca(' '))) or profundidade == 0:
        return peca_para_inteiro(obter_ganhador(t)), seq_movimentos
    else:
        p_adv = inteiro_para_peca(-peca_para_inteiro(j))  # obter peca adversario
        melhor_resultado = peca_para_inteiro(p_adv)  # atualizar melhor resultado
        posicoes_jogador = obter_posicoes_jogador(t, j)  # obter pos jogador
        posicoes_livres = obter_posicoes_livres(t)  # obter pos livres
        for posicao in posicoes_jogador:  # simular movimentos de todas posicoes
            posicoes_adjacentes = obter_posicoes_adjacentes(posicao)
            for adjacente in posicoes_adjacentes:  # simular movimento para adjac
                if posicao_no_tuplo(adjacente, posicoes_livres):
                    copia_t = cria_copia_tabuleiro(t)  # criar copia do tabuleiro
                    novo_movimento = (posicao, adjacente)  # guardar movimento 
                    copia_t = move_peca(copia_t, posicao, adjacente)  # obter tab
                    # chamada recursiva da funcao com novo tab e novo jogador
                    novo_resultado, nova_seq_movimentos = minimax(copia_t, \
                                                                  p_adv, profundidade - 1,
                                                                  seq_movimentos + novo_movimento)
                    # verificar se ramo da recursao e melhor do que os anteriores
                    if melhor_seq_movimentos == () or pecas_iguais(j, cria_peca( \
                            'X')) and novo_resultado > melhor_resultado or pecas_iguais( \
                            j, cria_peca('O')) and melhor_resultado > novo_resultado:
                        melhor_resultado, melhor_seq_movimentos = \
                            novo_resultado, nova_seq_movimentos  # se sim guardar seq
        return melhor_resultado, melhor_seq_movimentos  # devolver melhor seq


def dois_em_linha(t, j):
    # tabuleiro x peca -> posicao
    '''recebe um tabuleiro t e uma peca j de um jogador e devolve posicao livre
    de uma linha com duas pecas j ou tuplo vazio se nao existir posicao assim'''
    localizacao = ()
    for i in range(9):  # obter colunas e linhas (c / l) das pecas do jogador 
        pos = inteiro_para_posicao(i)
        if pecas_iguais(obter_peca(t, pos), j):  # verificar se posicao tem peca j
            localizacao += (obter_pos_c(pos), obter_pos_l(pos))  # guardar c e l
    for elemento in localizacao:  # verificar se jogador pode ganhar nas c / l
        if localizacao.count(elemento) == 2:  # verificar se c / l tem duas pecas
            if ord(elemento) > 96:
                string = '1'  # e coluna -> percorrer linhas
            else:
                string = 'a'  # e linha -> percorrer colunas
            vetor = obter_vetor(t, elemento)  # verificar se vetor tem pos livre
            if peca_no_tuplo(cria_peca(' '), vetor, 1) == 1:
                for i in range(3):  # obter coordenada desconhecida da pos livre
                    if pecas_iguais(vetor[i], cria_peca(' ')) or i == 2: break
                    string = chr(ord(string) + 1)  # passar para a posicao seguinte
                if ord(string) > 96:
                    posicao = cria_posicao(string, elemento)
                else:
                    posicao = cria_posicao(elemento, string)
                return posicao  # devolver a posicao
        else:
            localizacao = localizacao[1:]  # se nao excluir coluna / linha
    return ()  # se ciclo terminar devolver tuplo vazio


def fase_colocacao(t, j):
    # tabuleiro x peca -> posicao
    '''recebe um tabuleiro e uma peca e devolve um tuplo com uma posicao de
    acordo com a estrategia de colocacao de pecas do jogo do moinho'''

    def vitoria():
        # tabuleiro x peca -> posicao
        '''recebe tabuleiro e peca, representando um jogador, devolve posicao
        que permite ao jogador vencer ou tuplo vazio se tal nao e possivel'''
        return dois_em_linha(t, j)

    def bloqueio():
        # tabuleiro x peca -> posicao
        '''recebe tabuleiro e peca, representando um jogador, devolve posicao de
        vitoria do adversario ou tuplo vazio se este nao tem posicao vitoria'''
        return dois_em_linha(t, inteiro_para_peca(-peca_para_inteiro(j)))

    def posicao_estrategica():
        # tabuleiro -> posicao
        '''recebe tabuleiro t e devolve a primeira posicao livre do tabuleiro de
        acordo com uma lista de prioridade pre-estabelecida'''
        livres = obter_posicoes_livres(t)  # obter posicoes livres
        for i in [4, 0, 2, 6, 8, 1, 3, 5, 7]:  # estabelecer lista de prioridade
            posicao = inteiro_para_posicao(i)  # transformar elemento em posicao
            if posicao_no_tuplo(posicao, livres):
                return posicao  # devolver primeira posicao livre

    for funcao in [vitoria, bloqueio, posicao_estrategica]:  # lista de estrategias
        p = funcao()  # aplicar as estrategias segundo a prioridade estabelecida
        if p == (): continue
        return (p,)


def fase_movimentacao(t, j, nivel):
    # tabuleiro x peca x str -> posicao
    '''recebe um tabuleiro, uma peca e uma string nivel contendo o modo de jogo
    devolve um tuplo de posicoes que representa o movimento a realizar segundo
    a estrategia do modo de jogo,caso nao seja possivel mover uma peca, move a 
    primeira peca para a posicao por esta ja ocupada'''

    def facil_aux(*args):
        # tabuleiro x peca -> tuplo
        '''recebe tabuleiro e peca devolve None e movimento da primeira peca
        jogador para primeira pos adjacente segundo ordem de leitura tabuleiro
        ou tuplo vazio se nao ha movimento disponivel'''
        pos_jogador = obter_posicoes_jogador(t, j)  # obter posicoes jogador
        pos_livres = obter_posicoes_livres(t)  # obter posicoes livres
        for posicao in pos_jogador:  # para cada posicao jogador obter adjacentes
            pos_adjacentes = obter_posicoes_adjacentes(posicao)
            for adjacente in pos_adjacentes:  # verificar se adjacente e livre
                if posicao_no_tuplo(adjacente, pos_livres):
                    return (None, (posicao, adjacente))
        return ()  # devolver tuplo vazio se nao houver movimento disponivel

    d = {'facil': (facil_aux, None), 'normal': (minimax, 1), 'dificil': (minimax, 5)}
    if existe_movimento_disponivel(t, j):  # obter movimento
        seq_movimentos = (d[nivel][0](t, j, d[nivel][1], ()))[1]
        movimento = (seq_movimentos[0], seq_movimentos[1])
    else:  # caso em que nao ha movimentos disponiveis
        pos_jogador = obter_posicoes_jogador(t, j)
        movimento = (pos_jogador[0], pos_jogador[0])
    return movimento  # devolver movimento


def obter_movimento_auto(t, j, nivel):
    # tabuleiro x peca x str -> posicao
    '''recebe um tabuleiro t, uma peca j e uma string nivel contendo o modo de 
    jogo e devolve uma posicao de acordo com a estrategia de jogo'''
    if len(obter_posicoes_livres(t)) > 3:  # determinar fase do jogo
        return fase_colocacao(t, j)  # mais de 3 pos livres -> colocacao
    else:
        return fase_movimentacao(t, j, nivel)  # caso contrario -> movimentacao


def moinho(jog, nivel):
    # str x str -> str
    '''recebe duas cadeias de caracteres, jog, a representacao externa da peca
    com que deseja jogar o jogador humano, e nivel, o nivel de dificuldade do 
    jogo e devove a representacao externa da peca ganhadora'''

    def turno_aux(j, nivel, tipo):
        # peca x str x bool-> inteiro
        '''recebe peca, string contendo o nivel e um bool indicando se e o turno
        computador, devolve tuplo com peca do ganhador no turno e a negacao do
        bool recebido'''
        if tipo == 1:  # obter movimento e mostrar mensagem terminal se necessario
            print('Turno do computador (' + nivel + '):')
            mov = obter_movimento_auto(t, j, nivel)
        else:
            mov = obter_movimento_manual(t, j)
        if len(obter_posicoes_livres(t)) == 3:
            move_peca(t, mov[0], mov[1])
        else:
            coloca_peca(t, j, mov[0])  # executar movimento
        print(tabuleiro_para_str(t))  # mostrar tabuleiro com movimento no terminal
        return (obter_ganhador(t), not tipo)

    if jog in ['[X]', '[O]'] and nivel in ['facil', 'normal', 'dificil']:
        print('Bem-vindo ao JOGO DO MOINHO. Nivel de dificuldade ' + nivel + '.')
        t = cria_tabuleiro()  # criar novo tabuleiro
        print(tabuleiro_para_str(t))  # mostrar tabuleiro inicialmente vazio
        if jog == '[O]':
            auto, tipo = cria_peca('X'), True  # obter peca jogador auto
        else:
            auto, tipo = cria_peca('O'), False  # tipo determina quem joga
        humano = cria_peca(jog[1])  # obter peca jogador humano
        ganhador = cria_peca(' ')  # inicialmente nao ha vencedor
        while pecas_iguais(ganhador, cria_peca(' ')):
            if tipo == True:
                ganhador, tipo = turno_aux(auto, nivel, tipo)
            else:
                ganhador, tipo = turno_aux(humano, nivel, tipo)
        return peca_para_str(ganhador)
    else:
        raise ValueError('moinho: argumentos invalidos')
