# --- Números em Python - Import math | Vídeo-Aula ---
#
# ▶️ Canal YouTube: Automation and Data Science
#           url: https://www.youtube.com/channel/UCOGLG_-uQco3Z7YGXtbEbEg
#
#       👉  video: https://youtu.be/ZcOWT7qGB98
#
# 💡 Dica: converta para comentário as linhas de código que não ver representada na consola.
#          Exemplo: # print(canal)
#
# ✔️ Ajude o nosso canal de Educação:
#       Partilhe, Faça like e Comente.
#       Ajudar este canal é ajudar toda a comunidade.
#
# ---

# 1: Como importar um módulo em Python
import math

help('math')

# 2: Como usar uma função e constante de um módulo
a = 2

resultado = math.sqrt(a)    # exemplo para cálculo da raíz quadrada
resultado = math.exp(a)     # exemplo para cálculo de  e ^ 2

PI = math.pi

# Exemplo: log( ), log( , n), log2( ), log10( )
b = 2 ** 5

resultado = math.log(math.e)    # exemplo para cálculo de logaritmo de base e, tipicamente designado por ln( )
resultado = math.log(b, 2)      # exemplo para cálculo de logaritmo de base 2, equivalente math.log2(b)
resultado = math.log(b, 10)     # exemplo para cálculo de logaritmo de base 10, equivalente math.log10(b)


# Exemplo: comb(n, k)
n = 9
k = 2

resultado = math.comb(n, k)


# Exemplo: ceil( ) e floor( )
c = 0.5

resultado = math.ceil(c)    # exemplo para arrendondar para o menor número inteiro
resultado = math.floor(c)   # exemplo para arrendondar para o maior número inteiro


print(resultado)
