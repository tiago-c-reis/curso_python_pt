# Problema: Escreva um programa que recolha uma sequência de cadeia de ADN, e retorne a uma sequência de mARN

# Lógica:
#    1 - Recolher a sequência de cadeia de ADN por parte do utilizador
#    2 - Verificar se é uma sequência correcta (apenas pode conter as letras A,C,T,G)
#    3 - Substituir as ocorrências de T por U
#    4 - Imprimir a sequência de ARN na consola

# YouTube Channel: Automation and Data Science
#                  ▶️https://www.youtube.com/channel/UCOGLG_-uQco3Z7YGXtbEbEg

# URL do video associado ao problema:
# 👉 https:// 

# - - - - - - - - - - - - - - - - - - - - - - - -

dna_strand = input('Please, state the DNA sequence: ').upper().strip()

bases = set(dna_strand)

isCorrect = True
for base in bases:
    if base not in 'ACGT':
        print(f"{base!r} is not a valid letter. Detected at index position: {dna_strand.find(base)}")
        isCorrect = False
        break

if isCorrect:
    rna_seq = dna_strand.replace('T', 'U')
    print(f"Corresponding RNA sequence:\n{rna_seq}")
