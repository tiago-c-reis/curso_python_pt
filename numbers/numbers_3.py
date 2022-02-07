# --- Números em Python - Funções Nativas | Vídeo-Aula ---
#
# ▶️ Canal YouTube: Automation and Data Science
#           url: https://www.youtube.com/channel/UCOGLG_-uQco3Z7YGXtbEbEg
#
#       👉  video: https://www.youtube.com/watch?v=MHNblk_fgQU
#
# 💡 Dica: converta para comentário as linhas de código que não ver representada na consola.
#          Exemplo: # print(canal)
#
# ✔️ Ajude o nosso canal de Educação:
#       Partilhe, Faça like e Comente.
#       Ajudar este canal é ajudar toda a comunidade.
#
# ---

# 1-2: Função min() e max()
a = 2.8
b = 10

valor_min = min(a, b)
valor_max = max(a, b)

print(valor_min)
print(valor_max)

# 3: Função abs()
c = -2.5
d = 8.2
e = 5 + 2j

resultado = abs(c)  # subsitua a variável na função abs para ver os diferentes resultados

print(resultado)

# 4: Função round( , n)
f = 1.586

resultado = round(f)       # arrendonda f para um número inteiro
print(resultado)

resultado = round(f, 2)    # arrendonda f para um número com duas casas decimais
print(resultado)

# 4.1: A função round() arredonda sempre para o valor inteiro par
g = 0.5

resultado = round(g)       # arrendonda g para 0 (entre 0 e 1, retorna 0 que é par)
print(resultado)

g = 1.5

resultado = round(g)       # arrendonda g para 2 (entre 1 e 2, retorna 2 que é par)
print(resultado)

# 5-6: pow() e divmod()
h = 10
i = 2

resultado = pow(h, i)   # o mesmo que h ** i
print(resultado)

resultado = divmod(h, i)    # podemos também utilizar h // i para saber o quociente e h % i para saber o resto
