# --- Fluxo em Python - For, For-else e For-For | Vídeo-Aula ---
#
# ▶️ Canal YouTube: Automation and Data Science
#           url: https://www.youtube.com/channel/UCOGLG_-uQco3Z7YGXtbEbEg
#
#       👉  video: https://youtu.be/SqDZfEwwInw
#
# 💡 Dica: converta para comentário as linhas de código que não ver representada na consola.
#          Exemplo: # print(canal)
#
# ✔️ Ajude o nosso canal de Educação:
#       Partilhe, Faça like e Comente.
#       Ajudar este canal é ajudar toda a comunidade.
#
# ---

# 1: A limitação de if
var1, var2, var3 = 1, 2, 3

if var1 == 0:
    print(f'{var1 = } é um número par.')
else:
    print(f'{var1 = } é um número ímpar.')

# 2.1-2.3 Comando for. Exemplos: [], range( ) e str
sequencia = [var1, var2, var3]  # Exemplo de uma sequência como lista como sequência
for x in sequencia:
    print(x)

intervalo = range(0, 11, 2)     # Exemplo de uma sequência como intervalo de números inteiros
for x in intervalo:
    print(x)

canal = 'Automation'            # Exemplo de uma sequência como string
for x in canal:
    print(x)

# 3: Comando for, else
sequencia = range(0, 21)
for x in sequencia:
    print(x)
else:
    print('Fim de contagem')

# 4: Exercício: Fazer a soma de todos os valores entre 10 e 100. Utilize um statement for.
intervalo = range(10, 101)

resultado = 0
for x in intervalo:
    resultado += x

print(f'O meu resultado é {resultado}')


# 5: Combinar for e if
intervalo = range(10, 11)
for x in intervalo:
    if x > 5:
        print(f'O valor {x} é MAIOR do que 5')
    elif x < 5:
        print(f'O valor {x} é MENOR do que 5')


# 6: Exercício: Fazer a soma de todos os valores entre 10 e 100 apenas se forem par.
intervalo = range(10, 101)

resultado = 0
for x in intervalo:
    if x % 2 == 0:
        resultado += x

print(f'O meu resultado é {resultado}')


# 7: Exercício: Todas as coordenadas entre 0 e 5? Nested for statements
coord_x = coord_y = range(0, 6)

for x in coord_x:
    for y in coord_y:
        print(f'({x}, {y})')
    else:
        print('Acabou varrimento de y --------')


# 8: Padrões em consola:

# Repetir o padrão
# +
# ++
# +++
# ++++
# +++++
# ++++++
# +++++++

for linha in range(1,8):
    print('+' * linha)
