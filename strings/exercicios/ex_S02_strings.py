# --- Strings em Python - Introdução e Princípios Básicos | Vídeo-Aula ---
#
# ▶️ Canal YouTube: Automation and Data Science
#           url: https://www.youtube.com/channel/UCOGLG_-uQco3Z7YGXtbEbEg
#
#       👉  video-exercício: https://youtu.be/x1CI--h9h9Q
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
# (a) o número de 'A's e 'G's
# (b) o número total de bases
# (c) se a sequência pode ser de 'ARN'

# -------------

# Exercício S02
seq = 'gggtgcgacg attcattgtt'

## Soluções:
# (a)
# resultado = seq.upper().count('A')
# resultado = seq.upper().count('G')


# (b)
# resultado = len(seq.replace(' ', ''))


# (c)
resultado = seq.find('u')

print(resultado)
