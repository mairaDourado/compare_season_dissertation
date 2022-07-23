def main():
    from find_probe import probe
    probe("C1_prob.txt", "prob_list_C1.txt") # arquivo lista recebe a lista de probes
    from make_arq import main
    from find_peak import peak
    peak("expressao_C1.txt", "dados_C1.txt","zero_C1.txt")
    peak("expressao_C2.txt", "dados_C2.txt","zero_C2.txt")
    from compare_phase import main
main()
