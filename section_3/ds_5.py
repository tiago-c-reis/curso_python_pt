# --- Estrutura de Dados em Python - Performance: List & Tuple | Vídeo-Aula ---
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

from sys import getsizeof
import timeit

# Análise 1: Memória (sem elementos)
lista, tupla = [], ()

print('RESULTADO 1 '.ljust(30, '-'), end='\n')
print(f'Espaço >> list: {getsizeof(lista)} bytes | tuple: {getsizeof(tupla)} bytes')
print('-' * 30, end='\n\n')


# Análise 2: Memória (com elementos)
el = 0, 'A', 2.1, True, 4 + 2j, 1, 'B', 3.1, False

print('RESULTADO 2 '.ljust(30, '-'), end='\n')
for x in range(len(el)):
    lista += [el[x]]
    tupla += el[x],
    resultado = f'+{x+1} el. >> list: {getsizeof(lista)} bytes | tuple: {getsizeof(tupla)} bytes'
    print(resultado)
else:
    print('-' * 30, end='\n\n')


# Análise 3: Tempo de Execução (inicializar)
tempo_lista = timeit.timeit("[0, 'A', 2.1, True, 4 + 2j, 1, 'B', 3.1, False]") * 1000
tempo_lista = round(tempo_lista, 2)

tempo_tupla = timeit.timeit("(0, 'A', 2.1, True, 4 + 2j, 1, 'B', 3.1, False)") * 1000
tempo_tupla  = round(tempo_tupla, 2)

print('RESULTADO 3 '.ljust(30, '-'), end='\n')

print(f'Tempo Execução >> list: {tempo_lista} ms | tuple: {tempo_tupla} ms')
print('-' * 30, end='\n\n')
