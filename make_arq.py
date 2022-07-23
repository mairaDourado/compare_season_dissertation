def main():
    # Este programa identifica em dois arquivos com a expressão das probes (transcritos rítimicos de C1 e C2) um grupo de probes em uma lista.
   
    # A resposta do programa são quatro arquivos: (1) com a expressão em C1, (2) com o zero relativo de C1, (3) com a expressão em C2, (4) com o zero relativo de C2
    print("Início: make_arq")

    # Coleta de inverno ---C1........................................................................................................................
    nomeArq = "C1_ritm.txt" # abertura do arquivo de transcritos rítmicos de C1
    arq_C1 = open(nomeArq,'r',encoding = 'utf-8') #arquivo base
    
    nomeArq = "prob_list_C1.txt"
    arq_lista = open(nomeArq, 'r', encoding = 'utf-8') #arquivo com a lista de genes a serem procurados
    
    nomeArq = "expressao_C1.txt"
    arq_expC1 = open(nomeArq, 'w', encoding = 'utf-8') #arquivo final com expressão de C1

    nomeArq = "zero_C1.txt"
    arq_zeroC1 = open(nomeArq, 'w', encoding = 'utf-8') #arquivo com valor zero relativo de C1
    
   
    # transforma  a lista de genes a serem procurados em uma lista------------------------------------------------------------
    lista2 = []
    l2 = arq_lista.readline() # leitura da lista de probes a serem procuradas
    
  
    while l2:
        lista = l2.split()
        lista2.append(lista) 
        l2 = arq_lista.readline() 
    arq_lista.close() #fecha o arquivo
    size = len(lista2)
    #--------------------------------------------------------------------------------------------------------------------------

    # Escrevendo o arquivo de expressão de C1 ----------------------------------------------------------------------------------
    l1 = arq_C1.readline()
    arq_expC1.write(l1) # escrevendo o cabeçalho do arquivo
    
    col = 1 #determinando coluna com lista de probes no arquivo
    
    l1 = arq_C1.readline()
    lista1 = l1.split() # transforma a linha em uma lista
    n = 0


    inicio = 4 # inicio dos dados de expressão
    fim = 15 # fim dos dados de expressão

    # definição da maior e menor intensidade entre os timepoints das probes
    maior_C1 = float(lista1[inicio])
    menor_C1 = float(lista1[inicio])

    #procura do arquivo na lista
    n += 1
    cont = 0
        
    while cont < size:
            
        if lista2[cont][0] == lista1[col-1]:
            arq_expC1.write(l1)
                
            cont = size

            # Determinando se há maior e menor intendidade na linha
            for i in range (inicio, fim + 1, 1):
                if maior_C1 < float(lista1[i]):
                    maior_C1 = float(lista1[i])
                if menor_C1 > float(lista1[i]):
                    menor_C1 = float(lista1[i])
        else:
            cont += 1
            
    l1 = arq_C1.readline()

    while l1:
        n += 1
        lista1 = l1.split() # transforma a linha em uma lista
        cont = 0


        
        while cont < size:
            
            if lista2[cont][0] == lista1[col-1]:
                arq_expC1.write(l1)
                
                cont = size

                # Determinando se há maior e menor intendidade na linha

                for i in range (inicio, fim + 1, 1):
                    if maior_C1 < float(lista1[i]):
                        maior_C1 = float(lista1[i])
                    if menor_C1 > float(lista1[i]):
                        menor_C1 = float(lista1[i])
            else:
                cont += 1
        l1 = arq_C1.readline()
        

    arq_C1.close()
    arq_expC1.close()
    
    print("C1 escrito")
    print("Maior em C1: ", maior_C1)
    print("Menor em C1: ", menor_C1)
    print(n)
    
    # definição do zero
    media_C1 = (maior_C1 + menor_C1)/2
    arq_zeroC1.write(str(media_C1))
    arq_zeroC1.write("\nMaior: ")
    arq_zeroC1.write(str(maior_C1))
    arq_zeroC1.write("\nMenor: ")
    arq_zeroC1.write(str(menor_C1))
    arq_zeroC1.close()
    

    #---------------------------------------------------------------------------------------------------------------------------
    #................................................................................................................................

    # Coleta de verão----C2.............................................................................................................................
    nomeArq = "C2_ritm.txt" # abertura do arquivo de transcritos rítmicos de C2
    arq_C2 = open(nomeArq,'r',encoding = 'utf-8') #arquivo base
      
    nomeArq = "expressao_C2.txt"
    arq_expC2 = open(nomeArq, 'w', encoding = 'utf-8') #arquivo final com expressão de C2

    nomeArq = "zero_C2.txt"
    arq_zeroC2 = open(nomeArq, 'w', encoding = 'utf-8') #arquivo com valor zero relativo de C2
    

    # Escrevendo o arquivo de expressão de C2----------------------------------------------------------------------------------
    l1 = arq_C2.readline()
    arq_expC2.write(l1) # escrevendo o cabeçalho do arquivo
    
    col = 1 #determinando coluna com lista de probes no arquivo
    
    l1 = arq_C2.readline()
    lista1 = l1.split() # transforma a linha em uma lista
    n = 0


    inicio = 4 # inicio dos dados de expressão
    fim = 15 # fim dos dados de expressão

    # definição da maior e menor intensidade entre os timepoints das probes
    maior_C2 = float(lista1[inicio])
    menor_C2 = float(lista1[inicio])

    #procura do arquivo na lista
    n += 1
    cont = 0
        
    while cont < size:
            
        if lista2[cont][0] == lista1[col-1]:
            arq_expC2.write(l1)
                
            cont = size

            # Determinando se há maior e menor intendidade na linha
            for i in range (inicio, fim + 1, 1):
                if maior_C2 < float(lista1[i]):
                    maior_C2 = float(lista1[i])
                if menor_C2 > float(lista1[i]):
                    menor_C2 = float(lista1[i])
        else:
            cont += 1
            
    l1 = arq_C2.readline()

    while l1:
        n += 1
        lista1 = l1.split() # transforma a linha em uma lista
        cont = 0


        
        while cont < size:
            
            if lista2[cont][0] == lista1[col-1]:
                arq_expC2.write(l1)
                
                cont = size

                # Determinando se há maior e menor intendidade na linha

                for i in range (inicio, fim + 1, 1):
                    if maior_C2 < float(lista1[i]):
                        maior_C2 = float(lista1[i])
                    if menor_C2 > float(lista1[i]):
                        menor_C2 = float(lista1[i])
            else:
                cont += 1
        l1 = arq_C2.readline()
        

    arq_C2.close()
    arq_expC2.close()
    
    print("C2 escrito")
    print("Maior em C2: ", maior_C2)
    print("Menor em C2: ", menor_C2)
    print(n)
    
    # definição do zero
    media_C2 = (maior_C2 + menor_C2)/2
    arq_zeroC2.write(str(media_C2))
    arq_zeroC2.write("\nMaior: ")
    arq_zeroC2.write(str(maior_C2))
    arq_zeroC2.write("\nMenor: ")
    arq_zeroC2.write(str(menor_C2))
    arq_zeroC2.close()

    
    print("Fim: make_arq")
    #---------------------------------------------------------------------------------------------------------------------------
    #................................................................................................................................

main()
