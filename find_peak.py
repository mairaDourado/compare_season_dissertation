def peak(arq1, arq2, arq3):
        print("Inicio: find_peak")
        # Identificando os picos.........................................................................................................
        nomeArq = arq1 # abertura do arquivo de transcritos rítmicos
        arq_expC1 = open(nomeArq,'r',encoding = 'utf-8') #arquivo base1
        
        nomeArq = arq2
        arq_dados = open(nomeArq, 'w', encoding = 'utf-8') #arquivo final com expressão de C1

        nomeArq = arq3
        arq_zero = open(nomeArq, 'r', encoding = 'utf-8') #arquivo com valor zero relativo de C1


        # Pegando o zero
        lz = arq_zero.readline()
        linha_z = lz.split()
        print(linha_z)
        zero = float(linha_z[0])
        arq_zero.close()
        
        
        l1 = arq_expC1.readline()
        arq_dados.write(l1)
        head1 = l1.split()
        



        inicio = 4 # inicio dos dados de expressão
        fim = 15 # fim dos dados de expressão

        l1 = arq_expC1.readline()
        

        
        
        while l1:
                linha1 = l1.split()
                for i in range (inicio, fim + 1, 1):
                        linha1[i] = float(linha1[i])
                


                zt = inicio
            
                pico1 = 0
                n_pico1 = 0
            
                maior1 = linha1[zt]
                zt_maior1 = zt
                
                vale2 = 0
                n_vale2 = 0

                menor2 = linha1[zt]
                zt_menor2 = zt
            
                perfil1 = []
                for i in range( 0, 12, 1):
                        perfil1.append(2)
            

                resultado1 = []
                resultado2 = []
            
                 # determinação dos picos---------------------------------------------------------------------
                if linha1[inicio] > zero and linha1[fim] > zero:
                
                        while linha1[zt] > zero:
                                pico1 += 1
                                perfil1[zt - 4] = 1
                                x2 = zt
                                # determinação do zt do ápice do pico===========================================
                                if maior1 < linha1[zt]: 
                                        maior1 = linha1[zt]
                                        zt_maior1 = zt
                                            
                                #===============================================================================
                                zt += 1
                        zt = fim       
                        while linha1[zt] > zero:
                                pico1 += 1
                                perfil1[zt - 4] = 1
                                x1 = zt
                                # determinação do zt do ápice do pico===========================================
                                if maior1 < linha1[zt]: 
                                        maior1 = linha1[zt]
                                        zt_maior1 = zt
                                            
                                #===============================================================================
                                zt -= 1
                        zt = x2 + 1
                        n_pico1 += 1
                    
                        resultado1.append([pico1, maior1, zt_maior1, x1, x2])
                    
                        pico1 = 0
                        maior1 = linha1[zt]
                        zt_maior1 = zt
                    
                        stop = x1
                        while zt < stop:
                                if linha1[zt] > zero:
                                        x1 = zt
                                        while zt < stop and linha1[zt] > zero:
                                                pico1 += 1

                                                # determinação do zt do ápice do pico===========================================
                                                if maior1 < linha1[zt]: 
                                                        maior1 = linha1[zt]
                                                        zt_maior1 = zt
                                            
                                                #===============================================================================
                                                perfil1[zt - 4] = 1
                                                x2 = zt    # zt do fim do pico    
                                                zt += 1
                                        if pico1 >= 2:
                                                n_pico1 += 1
                                                resultado1.append([pico1, maior1, zt_maior1, x1, x2])
                                
                                        pico1 = 0
                                        maior1 = linha1[zt]
                                        zt_maior1 = zt
                        
                                else:
                                        y1 = zt    
                                        while  zt < stop and linha1[zt] <= zero:
                                                vale2 += 1
                                                # determinação do zt do mínimo do vale==========================================
                                                if menor2 > linha1[zt]:
                                                        menor2 = linha1[zt]
                                                        zt_menor2 = zt
                                                        
                                                #===============================================================================
                                                perfil1[zt - 4] = 0
                                                y2 = zt     # zt do fim do vale
                                                zt += 1
                                        if vale2 >= 2:
                                                n_vale2 += 1
                                                resultado2.append([vale2, menor2, zt_menor2, y1, y2])

                                        vale2 = 0
                                        menor2 = linha1[zt]
                                        zt_menor2 = zt
                    
                else:
                        while zt < fim + 1:
                        
                                if linha1[zt] > zero:
                                        x1 = zt
                                        while zt < fim + 1 and linha1[zt] > zero:
                                                pico1 += 1

                                                # determinação do zt do ápice do pico===========================================
                                                if maior1 < linha1[zt]: 
                                                        maior1 = linha1[zt]
                                                        zt_maior1 = zt
                                            
                                                #===============================================================================
                                                perfil1[zt - 4] = 1
                                                x2 = zt    # zt do fim do pico    
                                                zt += 1
                                        if pico1 >= 2:
                                                n_pico1 += 1
                                                resultado1.append([pico1, maior1, zt_maior1, x1, x2])
                                        if zt < fim + 1:

                                                pico1 = 0
                                                maior1 = linha1[zt]
                                                zt_maior1 = zt
                            
                                else:
                                        y1 = zt    
                                        while  zt < fim + 1 and linha1[zt] <= zero:
                                                vale2 += 1
                                                # determinação do zt do mínimo do vale==========================================
                                                if menor2 > linha1[zt]:
                                                        menor2 = linha1[zt]
                                                        zt_menor2 = zt
                                                        
                                                #===============================================================================
                                                perfil1[zt - 4] = 0
                                                y2 = zt     # zt do fim do vale
                                                zt += 1
                                        if vale2 == 1:
                                                if y1 == inicio or y1 == fim:
                                                        n_vale2 += 1
                                                        resultado2.append([vale2, menor2, zt_menor2, y1, y2])  
                                        if vale2 >= 2:
                                                n_vale2 += 1
                                                resultado2.append([vale2, menor2, zt_menor2, y1, y2])
                                        if zt < fim + 1:

                                                vale2 = 0
                                                menor2 = linha1[zt]
                                                zt_menor2 = zt
                    
            
                l1 = arq_expC1.readline()
                #escrita dos detalhes da probe----------------------------------------------
                for i in range(0, 4):
                        arq_dados.write(str(linha1[i]))
                        arq_dados.write(",")
                #---------------------------------------------------------------------------

                #escrita dos picos-----------------------------------------------------------
                arq_dados.write(str(n_pico1))
                arq_dados.write(str(","))
            
                for i in range(0,len(resultado1)):
                        arq_dados.write("pico ")
                        arq_dados.write(str(i))
                        arq_dados.write(",")
                    
                        for j in range(0, len(resultado1[0])):
                            
                                arq_dados.write(str(resultado1[i][j]))
                                arq_dados.write(",")
                #----------------------------------------------------------------------------

                #escrita do perfil-----------------------------------------------------------
                y = ""
                for i in range(0, 12):
                        y += str(perfil1[i])
                arq_dados.write(y)
                arq_dados.write(",")
                
                #escrita dos vales-----------------------------------------------------------
                arq_dados.write(str(n_vale2))
                arq_dados.write(str(","))
            
                for i in range(0,len(resultado2)):
                        arq_dados.write("vale ")
                        arq_dados.write(str(i))
                        arq_dados.write(",")
                    
                        for j in range(0, len(resultado2[0])):
                            
                                arq_dados.write(str(resultado2[i][j]))
                                arq_dados.write(",")
                #-----------------------------------------------------------------------------
                                
                arq_dados.write("\n")
            
            

        arq_expC1.close()
        arq_dados.close()
        print("Fim: find_peak")
                        
        return None
