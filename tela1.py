while True:    
    print('''=====================[MENU DE CONVERSÃO]=====================

                    -----------------------------
                    |    OPÇÃO    |    VALOR    |
                    -----------------------------
                    |     > 1     |   BINÁRIO   |
                    |     > 2     | OCTADECIMAL |
                    |     > 3     | HEXADECIMAL |
                    -----------------------------

=============================================================''')
    numDec_i = int(input('>> Digite um número inteiro: '))
    convType = int(input('>> Insira o tipo de conversão: '))

    if convType == 0:
        print("Programa encerrado")
        break
    
    while convType != 1 and convType != 2 and convType != 3:
        convType = int(input('<!> >> Opção inválida! Insira uma das opções da tabela: '))
        if convType == 1 or convType == 2 or convType == 3:
            break

    #FUNÇÃO DE PROCESSAMENTO DE ESCOLHA
    def convDecTo(numMultiplier):

        if numMultiplier == 2:
            abvName = 'BIN'
            extName = 'binário'
        elif numMultiplier == 8:
            abvName = 'OCT'
            extName = 'octadecimal'
        elif numMultiplier == 16:
            abvName = 'HEX'
            extName = 'hexadecimal'

        numDec = numDec_i
        numConverted = ''
        hexValue = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
        
        while numDec!=0:
            divRemainder = numDec%numMultiplier
            numConverted = hexValue[divRemainder] + numConverted
            numDec = numDec//numMultiplier

        print(f'''====================[CONVERSOR DEC > {abvName}]====================
    >> A conversão de {numDec_i} para {extName} é de {numConverted}.
    =============================================================''')

    #SAÍDA DE RESULTADO
    match convType:
        case 1:
            convDecTo(2)
        case 2:
            convDecTo(8)
        case 3:
            convDecTo(16)
    
    resposta = input("Deseja voltar ao Menu? (s/n) ? ")
    if resposta == "n":
        print("Programa encerrado")
        break