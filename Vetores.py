def proj_ortogonal(u,f):
    """
    Para calcular Proj_f(u), isto é, a projeção de u em f, a função deve 
    receber 2 variaveis: os vetores f e u.

    Proj_f(u) = (<u|f>)/||f||**2 * f

    Nesse caso: 

    <u|f> = u[0]*f[0] + u[1]*f]1 + ... + u[n-1]*f[n-1]

    ||f||**2 = (f[0])**2 + (f[1])**2 + ... + (f[n-1])**2

    COISO = <u|f>/||f||**2

    Se:
        f = [a,b,c, ... n-1ésimo]

    Então:
        Proj_f(u) = [a*COISO, b*COISO, ..., n-1ésimo*COISO] 
    """

    # Encontrar módulo de Proj.
    n = len(u)
    prod_escalar = float(0)
    modulo_f_quadrado = float(0)
    i = 0

    while i < n:
        prod_escalar = prod_escalar + (u[i]*f[i])
        modulo_f_quadrado = modulo_f_quadrado + ((f[i])**2)
        i = i + 1
    
    modulo = (prod_escalar)/(modulo_f_quadrado)
    
    # Agora que foi criado o módulo de Proj, criar a lista Proj.
    Proj = []
    i = 0

    while i < n:
        elemento = f[i]*modulo
        Proj.append(elemento)
        i = i + 1

    return Proj

def soma_vetores(A,B,op):
    """
    Dadas dois vetores A e B, somar ambos. A variável "op" é um indicador
    de operação, no qual:
        Se OP = 1, soma
        Se OP = 0, subtração
    """
    coord = len(A)
    i = 0

    S = []

    # Soma
    if op == 1:
        while i < coord:
            soma = A[i]+B[i]
            S.append(soma)
            i = i + 1

    # Subtração
    elif op == 0:
        while i < coord:
            soma = A[i]-B[i]
            S.append(soma)
            i = i + 1

    return S

def cria_matriz_caixa_preta(n):
    """
    Dado um tamanho n, criar um vetor com n elementos, todos eles sendo 0.
    """
    i = 0
    A = []

    while i < n:
        A.append(float(0))
        i = i + 1

    return A

def cria_f(U,F,n):
    """
    INPUT:
    Na main, haverá uma matriz U contendo todos os u's tal que U = [u1,u2,u3,...,un]. De mesmo modo, haverá
    uma matriz F contendo todos os f até o momento, tal que F = [f1,f2,f3,...,fk], sendo fk o último f sabido.
    Além disso, se receberá um n a fim de saber qual f estamos calculando.

    CONTA:
    f1 = u1
    f2 = u2 - Proj_f1(u2)
    f3 = u3 - Proj_f1(u3) - Proj_f2(u3)
    ()...)
    fn = un - Proj_f1(un) - Proj_f2(un) - ... Proj_f(n-1)(un)
    """
    coord = len(U[0])
    u = U[n-1]

    i = 0
    soma_Proj = cria_matriz_caixa_preta(coord)
    
    while i < (n-1):         
        P = proj_ortogonal(u,F[i])
        soma_Proj = soma_vetores(soma_Proj,P,1)
        i = i + 1

    f = soma_vetores(u,soma_Proj,0)

    return f

def cria_U_input_usuário(n):
    """
    O usuário pode digitar no teclado os valores que quiser. O indicador "n" serve para
    informar quantas dimensões se está trabalhando, isto é, quantos "u"s haverão e quantas
    coordenadas haverá em cada "u".
    """
    i = 0
    U = []

    # Cria-se um un.
    while i < n:
        U.append([])
        j = 0

        # Pergunta-se ao usuário quais são as coordenadas desse un.
        while j < n:
            U[i].append(float(input(f"Digite o {j+1}º elemento do vetor u{i+1}: ")))
            j = j + 1

        i = i + 1
    
    return U

def converte_para_ortonormal(F):
    """
    Para converter F = f1, f2, ..., fn em uma base E = e1, e2, ..., en ortonormal, 
    deve-se calcular o módulo de um f e dividir coordenadas do f correspondente.

    e_n = [ fn[0]*||fn|| , fn[1]*||fn|| , fn[2]*||fn|| , ... , fn[n-1]*||fn|| ]
    """
    n = len(F)          
    i = 0 
    E = []

    # Seleciona um en.
    while i < n:        
        E.append([])
        k = 0
        j = 0
        modulo_f_quadrado = 0

        # Calcula o módulo de fn
        while k < n:   
            modulo_f_quadrado = modulo_f_quadrado + ((F[i][k])**2)
            k = k + 1
        modulo_f = (modulo_f_quadrado)**(1/2)

        # Calcula as coordenadas do f correspondente dividas pelo módulo e adiciona à en.
        while j < n: 
            E[i].append(F[i][j]/modulo_f)
            j = j + 1
        i = i + 1

    return E

def main():
    print("Aviso! Os vetores digitados devem ser L.I..")
    n = int(input("Em qual dimensão estamos trabalhando?: "))
    if n > 0:
        U = cria_U_input_usuário(n)
        F = [U[0]]
        i = 2

        while i <= n:
            F.append(cria_f(U,F,i))
            i = i + 1

        E = converte_para_ortonormal(F)

        print(f"Os vetores de sua base ortonormal são {E}.")

    else:
        print("Inválido.")
        return

main()
