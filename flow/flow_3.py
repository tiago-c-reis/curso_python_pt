# --- Fluxo em Python - while e while-else | Vídeo Aula ---
#
# ▶️ Canal YouTube: Automation and Data Science
#           url: https://www.youtube.com/channel/UCOGLG_-uQco3Z7YGXtbEbEg?sub_confirmation=1
#
#       👉  video: hhttps://www.youtube.com/watch?v=c50yHlLdop0
#
# 💡 Dica: converta para comentário as linhas de código que não ver representada na consola.
#          Exemplo: # print(canal)
#
# ✔️ Ajude o nosso canal de Educação:
#       Partilhe, Faça like e Comente.
#       Ajudar este canal é ajudar toda a comunidade.
#
# ---

# 1: Compara if vs. while (ambos tem como inicialização uma condição)
cidade = 'Paris'

tentativa = input('Indique uma cidade do mundo: ')

if tentativa == cidade:
    print('Parabéns acertou!')
else:
    print('Errou.')


# 2: Definir while
cidade = 'Paris'

tentativa = input('Indique uma cidade do mundo: ')

while tentativa != cidade:
    tentativa = input('Indique uma cidade do mundo: ')

print('Parabéns acertou!')


# 3.1: Infinite loops
# Atenção⚠: O código abaixo está sob a forma de comentário. Para o correr remova as #s em cada linha.
#           Se ficar preso neste loop infinito faça CTRL + F2

# x = 8
# while x > 3:
#     print('Estou preso num while loop.')


# 3.2: Combinação while-else
x = 0

while x < 11:
    print(x)
    x += 1
else:
    print('Fim do statement while')


# Exercício: Desenvolva um jogo em que o user tem de adivinhar um número entre 0 e 10
#            > Conte o número de tentativas que foram utilizadas
#            > Dê indicações ao user: O número é maior/menor

resposta = 8

user, tentativa = -1, 0

while user != resposta:
    user = int(input('Indique um número entre 0 - 10: '))

    tentativa += 1

    if user > resposta:
        print('O valor indicado é MAIOR face a resposta', end='\n\n')
    elif user < resposta:
        print('O valor indicado é MENOR face à resposta', end='\n\n')
else:
    print(f'Parabéns acertou! O valor era {resposta}')
    print(f'Utilizou um total de {tentativa} tentativas.')


# Exercício: Qual a personagem do mundo Harry Potter?
#            Regras: Comece com o nome da personagem representado por '-'
#                    Um jogar vai indicando letras, e se essas letras estiverem presentes, substitua '-' pela letra.
#                    Conte o número de tentativas.

resposta = 'Hagrid'

user = '-' * len(resposta)
tentativa = 0

while user != resposta:
    letra = input('Indique uma letra: ')
    tentativa += 1

    if letra in resposta:
        idx = resposta.index(letra)
        user = user[0: idx] + letra + user[idx +1: ]

    print(user, end='\n\n')
else:
    print('Parabéns'.center(30, '*'))
    print(f'A personagem era {resposta}.')
    print(f'Foram utilizadas {tentativa} tentativas.')
    
