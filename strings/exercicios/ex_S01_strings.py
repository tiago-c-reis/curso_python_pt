# --- Strings em Python - Introdução e Princípios Básicos | Vídeo-Aula ---
#
# ▶️ Canal YouTube: Automation and Data Science
#           url: https://www.youtube.com/channel/UCOGLG_-uQco3Z7YGXtbEbEg
#
#       👉  video-exercício: https://youtu.be/WMSDqcgtwwo
#
# 💡 Dica: remova o # para ativar essa linha de código
#          Exemplo: # resultado = nome[0] ---> apenas: resultado = nome[0]
#
# ✔️ Ajude o nosso canal de Educação:
#       Partilhe, Faça like e Comente.
#       Ajudar este canal é ajudar toda a comunidade.
#
# -------------

# Indique:
# (a) o primeiro e último caractere
# (b) todos coracteres em índice par
# (c) a reversão da variável
# (d) como alterar o valor da variável nome para 'Piere Curie'

# -------------

# Exercício S01
nome = 'Marie Curie'

## Soluções:
# (a)
# resultado = nome[0]
# resultado = nome[-1]

# (b)
# resultado = nome[::2]

# (c)
# resultado = nome[::-1]

# (d)
resultado = nome.replace('Marie', 'Piere')

print(resultado)

