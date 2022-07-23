def main():
    # Este programa identifica em dois arquivos com a expressão das probes (transcritos rítimicos de C1 e C2) um grupo de probes em uma lista.
    # A cada probe identificada na lista, é identificado o pico de expressão, sua fase, seu período e se há alteração no ZT 18.7
    # A resposta do programa é um arquivos com a identificação dos picos e comparação entre C1 e C2
    print("Início: compare_phase")

    #abertura dos arquivos........................................................................................................................
    nomeArq = "dados_C1.txt"
    arq_C1 = open(nomeArq,'r',encoding = 'utf-8') #arquivo com picos de C1
    
    nomeArq = "dados_C2.txt"
    arq_C2 = open(nomeArq, 'r', encoding = 'utf-8') #arquivo com picos de C2
    
    nomeArq = "arq_final.txt"
    arq_comp = open(nomeArq, 'w', encoding = 'utf-8') #arquivo final com comparação entre C1 e C2

    #definição de variáveis........................................................................................................................
    porcent_pico1 = []
    for i in range( 0, 12, 1):
        porcent_pico1.append(0)

    porcent_pico2 = []
    for i in range( 0, 12, 1):
        porcent_pico2.append(0)

    zt18_pico1 = []
    for i in range( 0, 12, 1):
        zt18_pico1.append(0)

    zt18_pico2 = []
    for i in range( 0, 12, 1):
        zt18_pico2.append(0)

    zt18_vale1 = []
    for i in range( 0, 12, 1):
        zt18_vale1.append(0)

    zt18_vale2 = []
    for i in range( 0, 12, 1):
        zt18_vale2.append(0)

    n_pico1 = 0

    n_vale1 = 0

    n_nada1 = 0

    n_sonda = 0
    
    # leitura da linha: 0-nome, 1-coleta, 2-fase, 3-pico, 4-no de picos, 5-titulo do pico, 6-tamanho do pico, 7-maior intensidade, 8-zt da maior intensidade, 9-zt do inicio do pico, 10-zt do fim do pico, 11-perfil
    l1 = arq_C1.readline()
    head1 = l1.split()
    
    l2 = arq_C2.readline()
    head2 = l2.split()

    l1 = arq_C1.readline()
    l2 = arq_C2.readline()

    head3 = "Nome,zt inicio C1,zt fim C1,zt inicio C2,zt fim C2,período C1, período C2,diferença de período,zt int C1,zt int C2,diferença de fase,pico C1,pico C2,dif pico,ZT18 em C1,valor,ZT18 em C2,valor, amplitude C1, amplitude C2, diferença de amplitude"
    arq_comp.write(head3)
    arq_comp.write("\n")

   

    while l1:
        linha1 = l1.split(",")
        linha2 = l2.split(",")
        
        arq_comp.write(str(linha1[0]))
        arq_comp.write(", ")

        
        if linha1[4] == "1" and linha2[4] == "1":
            
            if linha1[0] == linha2[0]:
                # período-------------------------------------------------------------------------------------------------------
                z1 = int(linha1[9])
                z2 = int(linha1[10])
                y1 = float(head1[z1])
                y2 = float(head1[z2])
                
                
                arq_comp.write(str(y1)) #zt inicio C1
                arq_comp.write(", ")
                
                arq_comp.write(str(y2)) #zt fim C1
                arq_comp.write(", ")

                a1 = int(linha2[9])
                a2 = int(linha2[10])
                b1 = float(head2[a1])
                b2 = float(head2[a2])
                
                
                arq_comp.write(str(b1)) #zt inicio C2
                arq_comp.write(", ")
                
                arq_comp.write(str(b2)) #zt fim C2
                arq_comp.write(", ")

                
                if y2 > y1:
                    x1 = y2 - y1
                else:
                    x1 = (24 - y1) + y2

                arq_comp.write(str(x1)) #período C1
                arq_comp.write(", ")

                if b2 > b1:
                    x2 = b2 - b1
                else:
                    x2 = (24 - b1) + b2

                arq_comp.write(str(x2)) #período C2
                arq_comp.write(", ")
                   
                arq_comp.write(str(abs(x1 - x2))) #diferença de período
                arq_comp.write(", ")
                
                # fase----------------------------------------------------------------------------------------------------------
                y1 = int(linha1[8])
                y2 = int(linha2[8])
                
                z1 = float(head1[y1])
                arq_comp.write(str(z1)) #zt pico C1
                arq_comp.write(", ")
                
                z2 = float(head2[y2])
                arq_comp.write(str(z2)) #zt pico C2
                arq_comp.write(", ")
   
                fase = z1 - z2 # fase C1 - fase C2

                if fase > 12:
                    fase = -24 + fase #C1>C2 numericamente e C2 tem fase após C1 em uma ajuste de tempo de -12 a 12 com C1 como referência
                elif fase < -12:
                    fase = 24 + fase #C1<C2 numericamente e C2 tem fase antes C1 em uma ajuste de tempo de -12 a 12 com C1 como referência
                        
                    
                arq_comp.write(str(fase))#diferença de fase
                arq_comp.write(", ")

                x1 = int(linha1[3])
                x2 = int(linha2[3])
                
                arq_comp.write(str(x1)) #pico C1
                arq_comp.write(", ")
                arq_comp.write(str(x2)) #pico C2
                arq_comp.write(", ")
                arq_comp.write(str(x1 - x2))#dif pico
                arq_comp.write(", ")
                    
                

                # ZT 18 --------------------------------------------------------------------------------------------------------
                perfil = linha1[11] #C1
                p1 = perfil[9]
                p2 = perfil[11]
                p3 = perfil[10]
                
                if p1 == '0' and p2 == '0' and p3 == '1':
                    
                    arq_comp.write("pico,")
                    arq_comp.write('1')
                    arq_comp.write(", ")

                    zt18_pico1[int(linha1[8])-4] += 1
                    zt18_pico2[int(linha2[8])-4] += 1

                    n_pico1 += 1

                    
                elif p1 == '1' and p2 == '1' and p3 == '0':
                    arq_comp.write("vale,")
                    arq_comp.write('-1')
                    arq_comp.write(", ")

                    zt18_vale1[int(linha1[8])-4] += 1
                    zt18_vale2[int(linha2[8])-4] += 1

                    n_vale1 += 1
   
                else:
                    arq_comp.write("nada,")
                    arq_comp.write('0')
                    arq_comp.write(", ")

                    n_nada1 += 1

        

                perfil = linha2[11] #C2
                p1 = perfil[9]
                p2 = perfil[11]
                p3 = perfil[10]
                if p1 == '0' and p2 == '0' and p3 == '1':
                    arq_comp.write("pico,")
                    arq_comp.write('1')
                    arq_comp.write(", ")
                elif p1 == '1' and p2 == '1' and p3 == '0':
                    arq_comp.write("vale,")
                    arq_comp.write('-1')
                    arq_comp.write(", ")
                 
                else:
                    arq_comp.write("nada,")
                    arq_comp.write('0')
                    arq_comp.write(", ")

                #amplitude -------------------------------------------------------------
                #C1
                max1 = float(linha1[7])
                if linha1[12] == '1':
                    min1 = float(linha1[15])
                elif linha1[12] == '2':
                    min1 = min(float(linha1[15]),float(linha1[22]))
                elif linha1[12] == '3':
                    min1 = min(float(linha1[15]),float(linha1[22]), float(linha1[29]))
                amp1 = max1 - min1

                #C2
                max2 = float(linha2[7])
                if linha2[12] == '1':
                    min2 = float(linha2[15])
                elif linha2[12] == '2':
                    min2 = min(float(linha2[15]),float(linha2[22]))
                elif linha2[12] == '3':
                    min2 = min(float(linha2[15]),float(linha2[22]), float(linha2[29]))
                amp2 = max2 - min2
                
                #razão da amplitude C1/C2
                dif_amp = amp1/amp2
                arq_comp.write(str(amp1))
                arq_comp.write(", ")
                arq_comp.write(str(amp2))
                arq_comp.write(", ")
                arq_comp.write(str(dif_amp))
                arq_comp.write(", ")

                #calculos de porcentagem de picos com máximo no mesmo zt-------------------------------------------------------------------------------------
                n_sonda += 1

                porcent_pico1[int(linha1[8])-4] += 1
                porcent_pico2[int(linha2[8])-4] += 1

                
                #recomeço-------------------------------
        l1 = arq_C1.readline()
        l2 = arq_C2.readline()
        arq_comp.write("\n")
        
    print(n_sonda)
    arq_comp.write("\nPorcentagem de picos em C1\n")
    for i in range( 0, 12, 1):
        arq_comp.write(str(i))
        arq_comp.write(",")
    arq_comp.write("\n")
    for i in range( 0, 12, 1):
        arq_comp.write(str((porcent_pico1[i])/n_sonda))
        arq_comp.write(",")
    arq_comp.write("\n")

    arq_comp.write("\nPorcentagem de picos em C2\n")
    for i in range( 0, 12, 1):
        arq_comp.write(str(i))
        arq_comp.write(",")
    arq_comp.write("\n")
    for i in range( 0, 12, 1):
        arq_comp.write(str((porcent_pico2[i])/n_sonda))
        arq_comp.write(",")
    arq_comp.write("\n")

    arq_comp.write("\nPorcentagem de picos em C1 quando zt18 tem pico\n")
    for i in range( 0, 12, 1):
        arq_comp.write(str(i))
        arq_comp.write(",")
    arq_comp.write("\n")
    for i in range( 0, 12, 1):
        arq_comp.write(str((zt18_pico1[i])/n_sonda))
        arq_comp.write(",")
    arq_comp.write("\n")

    arq_comp.write("\nPorcentagem de picos em C2 quando zt18 tem pico\n")
    for i in range( 0, 12, 1):
        arq_comp.write(str(i))
        arq_comp.write(",")
    arq_comp.write("\n")
    for i in range( 0, 12, 1):
        arq_comp.write(str((zt18_pico2[i])/n_sonda))
        arq_comp.write(",")
    arq_comp.write("\n")

    arq_comp.write("\nPorcentagem de picos em C1 quando zt18 tem vale\n")
    for i in range( 0, 12, 1):
        arq_comp.write(str(i))
        arq_comp.write(",")
    arq_comp.write("\n")
    for i in range( 0, 12, 1):
        arq_comp.write(str((zt18_vale1[i])/n_sonda))
        arq_comp.write(",")
    arq_comp.write("\n")

    arq_comp.write("\nPorcentagem de picos em C2 quando zt18 tem vale\n")
    for i in range( 0, 12, 1):
        arq_comp.write(str(i))
        arq_comp.write(",")
    arq_comp.write("\n")
    for i in range( 0, 12, 1):
        arq_comp.write(str((zt18_vale2[i])/n_sonda))
        arq_comp.write(",")
    arq_comp.write("\n")
    
    arq_comp.write("número de picos em zt18: ,")
    arq_comp.write(str(n_pico1))
    arq_comp.write("\n")
    
    arq_comp.write("número de vales em zt18: ,")
    arq_comp.write(str(n_vale1))
    arq_comp.write("\n")

    arq_comp.write("ausência de pico e vale em zt18: ,")
    arq_comp.write(str(n_nada1))
    arq_comp.write("\n")
        
    arq_C1.close()
    arq_C2.close()
    arq_comp.close()
        
    print("Fim: compare_phase")

    
main()
    


    
