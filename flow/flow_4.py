# --- Fluxo em Python - break, continue e pass | Vídeo-Aula ---
#
# ▶️ Canal YouTube: Automation and Data Science
#           url: https://www.youtube.com/channel/UCOGLG_-uQco3Z7YGXtbEbEg
#
#       👉  video: https://youtu.be/HN0lLQKhjI8
#
# 💡 Dica: converta para comentário as linhas de código que não ver representada na consola.
#          Exemplo: # print(canal)
#
# ✔️ Ajude o nosso canal de Educação:
#       Partilhe, Faça like e Comente.
#       Ajudar este canal é ajudar toda a comunidade.
#
# ---

# 1: keyword -> break (combinado com statement for)
for x in range(0, 11):
    print(x)

    if x == 4:
        break
else:
    print('Varrimento concluído')

print(f'>> Último valor processado {x = }')


# 2: keyword -> break (combinado com statement while)
jogo, pontuação = 1, 0

while jogo < 11:
    if jogo == 3:
        break

    pontuação += 3
    print(f'JOGO #{jogo}: Pontuação atual = {pontuação}')
    jogo += 1
else:
    print('-' * 10)
    print(f'Pontuação Final = {pontuação}', end='\n\n')

print(' Pontuação Total '.center(30, '*'))
print(f'{pontuação} pontos.')


# 3: keyword -> continue (combinado com statement for)
for x in range(0, 11):
    if x % 2 == 0:
        continue

    print(x)
else:
    print('Varrimento concluído.')


# 4: keyword -> continue (combinado com statement while)
number = 0

while number < 10:
    number += 1

    if number % 2 == 0:
        continue

    print(number)
else:
    print('Statement else ativou')


# 5: keyword -> pass
for x in range(0, 11):
    print(x)
else:
    pass
