# --- Estrutura de Dados em Python - Lists: Introdução e Princípios | Vídeo-Aula ---
#
# ▶️ Canal YouTube: Automation and Data Science
#           url: https://www.youtube.com/channel/UCOGLG_-uQco3Z7YGXtbEbEg
#
#       👉  video: https://youtu.be/nuAV8-uqcfQ
#
# 💡 Dica: converta para comentário as linhas de código que não ver representada na consola.
#          Exemplo: # print(canal)
#
# ✔️ Ajude o nosso canal de Educação:
#       Partilhe, Faça like e Comente.
#       Ajudar este canal é ajudar toda a comunidade.
#
# ---


# 1: Como definir umalist (sequência mutável)
paciente = ['Ana', 34, 189.5, True]

print(paciente)
print(type(paciente))


# 2: Indexação de list
nome = paciente[0]
print(nome)

sublist = paciente[0:3]
print(sublist)


# 3: 2D list

resultados = [
    ['02/jan', 189.5],
    ['14/fev', 171.3],
    ['29/mar', 172.4],
    ['04/abr', 180.6]
]

for linha in resultados:
    print(linha[0])     # devolve todas as datas da 2D list resultados


data_interesse = resultados[0: 3: 2]
print(data_interesse)
print(type(data_interesse))

# 4: Mutabilidade
paciente = ['Ana', 34, 189.5, True]

print('Antes de mudar:')
print(paciente)

print('- '* 10)

paciente[0:2] = ['Tiago', 28]

print('Depois de mudar: ')
print(paciente)
