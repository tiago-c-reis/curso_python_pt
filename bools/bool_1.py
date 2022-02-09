# --- Booleanos em Python - Introdução e Operações ---
#
# ▶️ Canal YouTube: Automation and Data Science
#           url: https://www.youtube.com/channel/UCOGLG_-uQco3Z7YGXtbEbEg
#
#       👉  video: https://www.youtube.com/watch?v=YPK3tae3-VE
#
# 💡 Dica: converta para comentário as linhas de código que não ver representada na consola.
#          Exemplo: # print(canal)
#
# ✔️ Ajude o nosso canal de Educação:
#       Partilhe, Faça like e Comente.
#       Ajudar este canal é ajudar toda a comunidade.
#
# ---

# 1: Como definir um booleano em Python
mulher = True
gravidez = True

tipo = type(gravidez)

print(gravidez)
print(tipo)


# 2: Operações com booleanos (not, and e or)
# altere as variáveis mulher e gravidez nas linhas x e x para testar várias combinações

resultado = not mulher
print(resultado)

resultado = mulher and gravidez
print(resultado)

resultado = mulher or gravidez
print(resultado)


# 3: Comparações Parte I (>=, >, <=, <, ==, !=)
# altere as variáveis a e b nas linhas x e x para testar várias combinações
a = 5
b = 10

resultado = a >= b
print(resultado)

resultado = a <= b
print(resultado)

resultado = a == b
print(resultado)

resultado = a != b
print(resultado)


# altere as variáveis c e d nas linhas x e x para testar várias combinações
c = 'Ana'
d = 'Rui'

resultado = c >= d
print(resultado)

resultado = c <= d
print(resultado)

resultado = c == d
print(resultado)

resultado = c != d
print(resultado)

# 3: Comparações Parte II (is, is not)
# altere as variáveis a e b nas linhas x e x para testar várias combinações
a = 3
b = 3.0

resultado = a == b
print(resultado)

resultado = a is b
print(resultado)

resultado = a is not b
print(resultado)

# altere as variáveis a e b nas linhas x e x para testar várias combinações
c = 'Tiago'
d = 'Tiago'

resultado = c == d
print(resultado)

resultado = c is d
print(resultado)
