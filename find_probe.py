def probe(a1, a2):
    
    print("Início: find_probe")
    nomeArq = a1 # abertura dos arquivos
    arq1 = open(nomeArq,'r',encoding = 'utf-8') #arquivo base
    nomeArq = "lista.txt"
    arq2 = open(nomeArq, 'r', encoding = 'utf-8') #arquivo com a lista de genes a serem procurados
    nomeArq = a2
    arq3 = open(nomeArq, 'w', encoding = 'utf-8') #arquivo final

    # transforma  a lista de genes a serem procurados em uma lista
    lista2 = []
    l2 = arq2.readline() # leitura da lista de probes a serem procuradas
  
    while l2:
        lista = l2.split()
        lista2.append(lista) 
        l2 = arq2.readline() 
    arq2.close() #fecha o arquivo
    size = len(lista2)
    
    

        
    col = 1 #determinando coluna com lista de probes no arquivo
    l1 = arq1.readline()
    n = 0

    #procura do arquivo na lista

    while l1:
        n += 1
        lista1 = l1.split() # transforma a linha em uma lista
        cont = 0
        
        while cont < size:
            
            if lista2[cont][0] == lista1[col - 1]:
                arq3.write(lista1[col])
                arq3.write("\n")
                cont = size
            else:
                cont += 1
        l1 = arq1.readline()

    arq1.close()
    arq3.close()
    print("Fim: find_probe")
    print(n)

    return None
        
