# --- Strings em Python - Introdução e Princípios Básicos | Vídeo-Aula ---
#
# ▶️ Canal YouTube: Automation and Data Science
#           url: https://www.youtube.com/channel/UCOGLG_-uQco3Z7YGXtbEbEg
#
#       👉  video: https://youtu.be/vd_87mo234s
#
# 💡 Dica: converta para comentário as linhas de código que não ver representada na consola.
#          Exemplo: # print(canal)
#
# ✔️ Ajude o nosso canal de Educação:
#       Partilhe, Faça like e Comente.
#       Ajudar este canal é ajudar toda a comunidade.
#
# ---

# 1. Como definir str em Python (via ' ou " )
'Automation and Data Science'
"Automation and Data Science"

# 2. Como declarar/iniciar uma variável do tipo str
canal = 'Automation and Data Science'

# 3. Como imprimir na consola uma str
print(canal)
print()  # >> como imprimir uma linha vazia

tipo_conteudo = 'Tutorial'
nome_conteudo = 'Strings em Python - Princípios e Operações Básicas | Tutorial'

# >> print(arg0, arg1, ...) imprime numa linha cada argumento detectado
print(tipo_conteudo, nome_conteudo)
print()

# >> print(arg0, arg1, ..., sep=char, end=\char)
#    i)  o termo sep indica a str que deve se adicionada entre os argumentos
#        se não definido, o valor de defeito é uma espaço em branco
#    ii) o termo end indica a str que deve se adicionada no final da impressão na consola
#        se não definido, o valor de defeito é uma nova linha '\n'
print(tipo_conteudo, nome_conteudo, sep=':')
print()
print(tipo_conteudo, nome_conteudo, sep=' >> ', end=' ***')
print()

# 4. Definir uma variável str com várias linhas (via ''' ou """ )
canal_info = '''
Canal: Automation and Data Science
    Vídeo >> Tipo de Dados: Strings em Python
    Playlist >> Curso de Python Completo para Iniciantes
'''
print(canal_info)

# >> Dica: Por vezes a nossa str é bastante grande. De forma a conseguir ler confortávelmente no editor, podemos
#          escrever a str em multiplas linhas, mas não iremos imprimir essas linhas.
description_video = (
    'Como instalar Python e PyCharm num computador Windows.'
    ' Se tem um computador com sistema operativo Windows, neste tutorial aprenda a:'
    ' (1) verificar se #Python já está instalado num computador #Windows'
    ' (2) instalar Python no seu computador (se ainda não estiver instalado)'
    ' (3) instalar #PyCharm no seu computador'
)

print(description_video)
print()

# 5. Utilizar o caractere especial \ (escape character)
# >> imprimir novas linhas (\n)
#    nota: ao imprimir \n no final da str, podemos deixar de imprimir linhas vazias via print()
print('Strings em Python são um tipo de dados referentes a informação textual.\n\nAcabámos de criar duas linhas.', '\n')

# >> imprimir tabulações para melhor legibilidade (\t)
print('Canal\tSubscrever Canal\tAtivar Notificações', '\n')

# >> imprimir o caractere ' quando também é utilizado da definição da str
print('Número de visualizações: 1\'250 000', '\n')

# >> imprimir o caracter \ quando é utilizado na própria str (conceito de raw string)
print(r'c:\User\Ana', '\n')

# >> imprimir characteres with 32-bit hex value (exemplo: emoji)
print('\U0001F642', '\n')

# 6. Operações como str
# >> Concatenação (juntar várias str)
channel_part1 = 'Auto'
channel_part2 = 'mation'

concat = channel_part1 + channel_part2
print(concat, '\n')

# >> Multiplicação (repetir várias vezes uma str)
letter = '!'
print(letter * 3, '\n')

# >> Concatenação e Multiplicação
result = channel_part1 + channel_part2 + letter * 3
print(result, '\n')

# 7. Indexação (str são sequências de caracteres / formato [start:end:step] )
channel_name = 'Automation and Data Science'

# >> primeiro caractere
print(channel_name[0], '\n')

# >> primeiros 4 caracteres
print(channel_name[0:4], '\n')

# >> caracteres entre o 13º e 21º índice
print(channel_name[12:22], '\n')

# >> caracteres entre o 2º e 21º índice de 2 em 2 caracteres
print(channel_name[1:22:2], '\n')

# >> nota: caso início, fim e passo não estão indicados, estes assument o valor de 0, último índice e 1, respectivamente
print(channel_name[::], '\n')

# >> nota: usar índices negativos indica que estamos a correr a string da direita para a esquerda
# >> último caractere
print(channel_name[-1], '\n')

# >> últimos 10 caracteres
print(channel_name[-10:], '\n')

# >> reverter toda a str
print(channel_name[::-1], '\n')

# 8. Imutabilidade
# >> strings em Python são emutáveis, isso quer dizer que não podemos substituir caracteres individualmente

# channel_name[0] = 'B'  # Esta mensagem gera um erro do tipo TypeError, não podemos alterar 'A' por 'B'

# >> nota: podemos fazer a substituição de um caracter por outro da seguinte forma
letter = 'B'
result = letter + channel_name[1:]
print(result, '\n')

# 9. Format strings
# >> existe um subtipo de strings em Python chamadas formated strings, ou simplesmente, f strings
#    f strings permitem tratar informação dentro de uma string sob a forma de uma variável. O que é importante para
#    escrever scripts
user = 'Tiago'
formated_string = f"Olá {user}"
print(formated_string, '\n')

# >> outro exemplo das f strings é ter acesso ao nome da variável e seu valor str
print(f"{user = }")

# 10. Representation of strings ({var_name}!r ou repr(var_name))
# >>  Prints the string with the character ' included
user = 'Tiago'
print(f"{user!r}", '\n')  # opção 1
print(repr(user), '\n')  # opção 2

# 11. Comprimento de uma string, ou seja, número de caracteres numa string (via len())
channel_name = 'Automation and Data Science'
numero_caracteres = len(channel_name)

print(f'A string {channel_name!r} tem {numero_caracteres} caracteres')
