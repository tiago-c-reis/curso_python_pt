# --- Strings em Python - Introdução e Princípios Básicos | Vídeo-Aula ---
#
# ▶️ Canal YouTube: Automation and Data Science
#           url: https://www.youtube.com/channel/UCOGLG_-uQco3Z7YGXtbEbEg
#
#       👉  video-exercício: https://youtu.be/iB2I9qXCrm8
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
# (a) se o a variável email é um email correto
# (b) a correção do email em que '2' deve ser '@'
# (c) a corcorreção do email em que '.org' deve ser '.com'

# -------------

# Exercício S03
email = 'ana2automation.org'

## Soluções:
# (a)
# resultado = email.find('@')


# (b)
# resultado = email.replace('2', '@')


# (c)
resultado = email.replace('2', '@').replace('.org', '.com')

print(resultado)
