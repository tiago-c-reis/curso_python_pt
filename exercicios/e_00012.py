# Python - Exercícios do Curso de Python completo para Iniciantes
# 
# Desenhar balizas
#
# ▶️ Canal YouTube: Automation and Data Science
#           url: https://www.youtube.com/channel/UCOGLG_-uQco3Z7YGXtbEbEg
#
#       👉  video: https://youtu.be/UjOOSMRjr7U
#
# 💡 Dica: converta para comentário as linhas de código que não ver representada na consola.
#          Exemplo: # print(canal)
#
# ✔️ Ajude o nosso canal de Educação:
#       Partilhe, Faça like e Comente.
#       Ajudar este canal é ajudar toda a comunidade.
#
# code: e_00012
#
# ---

import re

c = '╔', '═', '╗', '║', '╎'
comprimento = 32

def posição(num, colunas):
    x = 2 * (num // colunas)
    y = num % colunas

    print(x, y)
    return x, y


def desenhar(colunas:int, pos:int):
    # Calcular vazio (dimensão da área)
    vazio = (comprimento - 2) // colunas

    x, y = posição(pos, colunas)

    # Primeira linha
    k = (comprimento - 2) + (colunas - 1) - (comprimento - 2) % colunas
    sup = c[0] + c[1] * k + c[2]
    print(sup)

    # Restantes linhas (Vamos considerar 6 linhas de altura)
    for i in range(6):
        espaço = (' ' * vazio + c[4]) * colunas
        linha = c[3] + espaço[:-1] + c[3]

        # Linhas ímpares: substituir ' ' por '.'
        if i % 2 != 0:
            linha = re.sub(' ', '.', linha)

        if i == x:
            _r = [31, 32]
            r = f'X'
            linha = linha[:(y + 1) * vazio] + 'X' + linha[(y + 1) * vazio + 1 :]

        print(linha)


# Executar a função:
for exemplo in range(1, 6):
    print(f'Baliza com {exemplo} colunas.')
    desenhar(exemplo)
    print('\n\n')
