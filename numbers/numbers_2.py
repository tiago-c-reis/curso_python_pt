# --- Números em Python - Operações e Métodos | Vídeo-Aula ---
#
# ▶️ Canal YouTube: Automation and Data Science
#           url: https://www.youtube.com/channel/UCOGLG_-uQco3Z7YGXtbEbEg
#
#       👉  video: https://youtu.be/QlXSXsJnJxs
#
# 💡 Dica: converta para comentário as linhas de código que não ver representada na consola.
#          Exemplo: # print(canal)
#
# ✔️ Ajude o nosso canal de Educação:
#       Partilhe, Faça like e Comente.
#       Ajudar este canal é ajudar toda a comunidade.
#
# ---

# 1: Operações algébricas ( + , - , * , / )
a = 10
b = 2

resultado = a + b   # soma
resultado = a - b   # subtração
resultado = a * b   # multiplicação
resultado = a / b   # divisão

tipo = type(resultado)


# 2: Outras operações ( // , % , ** )

resultado = a // b  # determinar quociente
resultado = a % b   # determinar resto
resultado = a ** b  # exponenciação, como referência a^(b)

a = 11
b = 0.5
c = 5

resultado = a + b * c           # multiplicações e divisões têm precedência sobre somas e subtrações
resultado = ( a + b ) * c       # a utilização de parêntesis curvos quebra essa precedência

# 3: .as_integer_ratio() e .is_integer()

resultado = b.as_integer_ratio()    # retorna dois números inteiros que representam a fração correspondente
resultado = b.is_integer()          # verifica se pode ser um int --> Falso
resultado = c.is_integer()          # verifica se pode ser um int --> True

print(resultado)
print(tipo)
