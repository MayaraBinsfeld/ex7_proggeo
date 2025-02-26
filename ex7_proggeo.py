"""
Programa: ex7_proggeo
Descrição: Este programa calcula progressões geométricas
Autor: Mayara Binsfeld
Data: 26/02/2025
Versão: 0.0.1

"""

# Alocação de memória

n_termo = 0
soma_termos = 0
primeiro_termo = 0
razao = 0
soma = 0
n_esimo = 0


# Entrada de dados 

primeiro_termo = int(input("Qual o primeiro termo da progressão?"))
razao = int(input("Qual a razão da progressão?"))
n_termo = int(input("Qual o numero de termos da progressão?"))



# Processamento de dados

soma = (((primeiro_termo * (razao**n_termo - 1)) / razao - 1))
n_esimo = (primeiro_termo * razao**(n_termo - 1))


# Saída de dados

print(f"O n-ésimo termo é {n_esimo} e a soma dos termos é {soma}")