# --- Fluxo em Python - If, elif e else | Vídeo-Aula ---
#
# ▶️ Canal YouTube: Automation and Data Science
#           url: https://www.youtube.com/channel/UCOGLG_-uQco3Z7YGXtbEbEg
#
#       👉  video: https://youtu.be/vDFSdzxa1II
#
# 💡 Dica: converta para comentário as linhas de código que não ver representada na consola.
#          Exemplo: # print(canal)
#
# ✔️ Ajude o nosso canal de Educação:
#       Partilhe, Faça like e Comente.
#       Ajudar este canal é ajudar toda a comunidade.
#
# ---

# 1: Comando if
x = 6   # Depois de 6, experimente com 2 e 8

if x > 5:
    print(x)


# 2: Comando if, else
nota = 20   # Depois de 20, experimente com 16 e 8

if nota >= 10:
    print(f'O aluno passou à disciplina, com a nota {nota}')
else:
    print(f'O aluno NÃO passou à disciplina, com a nota {nota}')


# 3: Exercício número par? Função input( )
numero = int(input('Qual é o número? '))    # Experimente 252 e 367

if numero % 2 == 0:
    print(f'{numero = } é um número par.')
else:
    print(f'{numero = } é um número ímpar.')


# 4: Comando if, else e elif
valor = 20  # Depois de 20, experimente com 16, 11 e 8

# Se um aluno tiver entre 20 - 18 tem nota 'A'
# Se um aluno tiver entre 17 - 15 tem nota 'B'
# Se um aluno tiver entre 14 - 10 tem nota 'C'
# Se um aluno tiver entre 9 - 0 tem nota 'D'

if valor >= 18:
    print('Nota A')
elif 15 <= valor <= 17:
    print('Nota B')
elif 10 <= valor <= 14:
    print('Nota C')
else:
    print('Nota D')


# 5: one-liner
idade = int(input('Qual a sua idade? '))    # Experimente na consola, 80, 50, 18 e 5

resultado = 'Senior' if idade >= 65 else 'Adulto' if 18 <= idade < 65 else 'Junior'

print(resultado)
