# --- Fluxo em Python - match l Vídeo Aula Curso de Python para Iniciantes
#
# ▶️ Canal YouTube: Automation and Data Science
#           url: https://www.youtube.com/channel/UCOGLG_-uQco3Z7YGXtbEbEg?sub_confirmation=1
#
#       👉  video: https://youtu.be/qs10eIfLm5g
#
# 💡 Dica: converta para comentário as linhas de código que não ver representada na consola.
#          Exemplo: # print(canal)
#
# ✔️ Ajude o nosso canal de Educação:
#       Partilhe, Faça like e Comente.
#       Ajudar este canal é ajudar toda a comunidade.
#
# ---


# 1: Como definir um statement match
val = int(input('Indique um dígito de 0 a 9: '))

match(val):
  case 0:
    mensagem = 'Selecionado o caso 0'
  case 1:
    mensagem = 'Seleccionado o caso 1'
  case _:
    mensagem = 'Seleccionado o caso geral, ou seja, tudo que não 0 ou 1'

print(mensagem)

# 2: Definir um statement match e |
animal = input('Indique um animal: ')

match(animal):
    case 'cão' | 'gato' | 'elefante':
        patas = 4
    case 'galinha' | 'pardal':
        patas = 2
    case _:
        patas = 0

print('RESPOSTA'.center(20, '-'))

if patas != 0:
    print(f'{animal} tem {patas} patas.')
else:
    print('Não conheço esse animal.')


# 3: Definir um statement match e condições guard
lados = int(input('Quantos lados devo considerar? '))

a = float(input('Qual o valor de a em (cm)? '))
b = float(input('Qual o valor de b em (cm)? '))

match(lados):
    case 3:
        forma, area = 'triângulo', a * b / 2
    case 4 if a == b:
        forma, area = 'quadrado', a ** 2
    case 4:
        forma, area = 'rectângulo', a ** 2

print('\n', 'RELATÓRIO'.center(20, '*'))

if forma:
    area = round(area, 2)
    print(f'A {forma = } tem área cm\u00b2')
else:
    print('Não consegui processar a sua forma')
    
