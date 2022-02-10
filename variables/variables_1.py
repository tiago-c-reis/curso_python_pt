# --- Variáveis em Python - Introdução e Técnicas | Vídeo-Aula ---
#
# ▶️ Canal YouTube: Automation and Data Science
#           url: https://www.youtube.com/channel/UCOGLG_-uQco3Z7YGXtbEbEg
#
#       👉  video: https://youtu.be/N6jTOx667UY
#
# 💡 Dica: converta para comentário as linhas de código que não ver representada na consola.
#          Exemplo: # print(canal)
#
# ✔️ Ajude o nosso canal de Educação:
#       Partilhe, Faça like e Comente.
#       Ajudar este canal é ajudar toda a comunidade.
#
# ---

# 1: Como iniciar/declarar uma variável em python
canal = 'Automation and Data Science'
meu_canal = 'Automation and Data Science'

print(canal)


# 2: Escolher o nome da variável

meu_canal = 'Automation and Data Science'
print(meu_canal)

# Exemplo de nomes errados para variáveis: 8canal, meu canal, meu@canal, meu!canal


# 3: Iniciar várias variáveis ao mesmo tempo
aluno, nota, disciplina, passou = 'Tiago', 20, 'Data Science', True

print(aluno)
print(nota)
print(disciplina)
print(passou)


# 4: Iniciar várias variáveis ao mesmo tempo e com o mesmo valor
Tiago_passou = Ana_passou = Sofia_passou = True

print(Tiago_passou)
print(Ana_passou)
print(Sofia_passou)


# 5: Apagar uma variável: del
nota = 18

print(nota)

del nota    # Após esta linha, vamos ter um erro na linha 37

# print(nota) # remover # para correr o código
