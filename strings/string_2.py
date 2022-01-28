# --- Strings em Python - Métodos Essenciais | Vídeo-Aula ---
#
# ▶️ Canal YouTube: Automation and Data Science
#           url: https://www.youtube.com/channel/UCOGLG_-uQco3Z7YGXtbEbEg
#
#       👉  video: https://youtu.be/QRBY0tIUBVo
#
# 💡 Dica: converta para comentário as linhas de código que não ver representada na consola.
#          Exemplo: # print(canal)
#
# ✔️ Ajude o nosso canal de Educação:
#       Partilhe, Faça like e Comente.
#       Ajudar este canal é ajudar toda a comunidade.
#
# ---

# 1-3: .strip(), lstrip() e .rstrip()
email = ' tiago@automation.com '

resultado_1 = email.strip(' ')
resultado_2 = email.lstrip(' ')
resultado_3 = email.rstrip(' ')

print(resultado_1)
print(resultado_2)
print(resultado_3)

# 4-5: .removeprefix() e .removesuffix()
website = 'www.google.com'

resultado_4 = website.removesuffix('www.')
resultado_5 = website.removesuffix('.com')

print(resultado_4)
print(resultado_5)

resultado_4e5 = website.removesuffix('www.').removesuffix('.com')

print(resultado_4e5)

# 6: .replace()
email = 'tiago@automation.com'

resultado_6_1 = email.replace('tiago', 'ana')
resultado_6_2 = email.replace('@', '+')
resultado_6_3 = email.replace('@', '')

print(resultado_6_1)
print(resultado_6_2)
print(resultado_6_3)

# 7-8: .split() e .rsplit()
# vamos utilizar o valor da linha 45, email = 'tiago@automation.com' (como está definida, não precisamos de
# escrever novamente

resultado_7_1 = email.split('@')

print(resultado_7_1)

canal = 'Automation and Data Science'

resultado_7_2 = canal.split(' ', maxsplit=2)
resultado_8 = canal.rsplit(' ', maxsplit=2)

print(resultado_7_2)
print(resultado_8)

# 9: .join()
termo = 'Conteúdo:'
valor = 'Data Science'
valor_2 = 'Machine Learning'

resultado_9 = ' '.join([termo, valor, valor_2])

print(resultado_9)

# 10-13: .upper(), .lower(), .capitalize() e .title()
# vamos utilizar o valor da linha 60, canal = 'Automation and Data Science'
# (como está definida, não precisamos de escrever novamente)

resultado_10 = canal.upper()
resultado_11 = canal.lower()
resultado_12 = canal.capitalize()
resultado_13 = canal.title()

print(resultado_10)
print(resultado_11)
print(resultado_12)
print(resultado_13)

# 14-16: .isupper(), .islower() e .istitle()
# vamos utilizar o valor da linha 60, canal = 'Automation and Data Science'
# (como está definida, não precisamos de escrever novamente)

resultado_14 = canal.isupper()
resultado_15 = canal.islower()
resultado_16 = canal.istitle()

print(resultado_14)
print(resultado_15)
print(resultado_16)

# vamos criar um resultado Verdadeiro (True)
resultado_14_1 = canal.upper().isupper()
print(resultado_14_1)

# 17-19: .isalpha(), .isnumeric() e .isalnum()
exemplo_a = 'Tiago'
exemplo_b = 'Tiago20'
exemplo_c = '20'
exemplo_d = 'Tiago 20'

print(exemplo_a.isalpha()) # Vamos ter como resposta True
print(exemplo_b.isalpha()) #   "    "    "     "     False
print(exemplo_c.isalpha()) #   "    "    "     "     False
print(exemplo_d.isalpha()) #   "    "    "     "     False

print(exemplo_a.isnumeric()) # Vamos ter como resposta False
print(exemplo_b.isnumeric()) #   "    "    "     "     False
print(exemplo_c.isnumeric()) #   "    "    "     "     True
print(exemplo_d.isnumeric()) #   "    "    "     "     False

print(exemplo_a.isalnum()) # Vamos ter como resposta True
print(exemplo_b.isalnum()) #   "    "    "     "     True
print(exemplo_c.isalnum()) #   "    "    "     "     True
print(exemplo_d.isalnum()) #   "    "    "     "     False

# 20: .count()
seq_adn = 'AAATGCATCGACTGATATGCGCATG'

resultado_20_1 = seq_adn.count('A')
resultado_20_2 = seq_adn.count('T')
resultado_20_3 = seq_adn.count('AT')
resultado_20_4 = seq_adn.count('U')

print(resultado_20_1)
print(resultado_20_2)
print(resultado_20_3)
print(resultado_20_3)

# 21-22: .find() e .rfind()
# vamos utilizar o valor da linha 129, seq_adn = 'AAATGCATCGACTGATATGCGCATG'
# (como está definida, não precisamos de escrever novamente)

resultado_21_1 = seq_adn.find('A')
resultado_21_2 = seq_adn.find('T')
resultado_21_3 = seq_adn.find('CA')
resultado_21_4 = seq_adn.find('U')

print(resultado_21_1)
print(resultado_21_2)
print(resultado_21_3)
print(resultado_21_3)

resultado_21_1_1 = seq_adn.find('A', 3)
print(resultado_21_1_1)

resultado_22 = seq_adn.rfind('A')
print(resultado_22)

# 23: .index()
# vamos utilizar o valor da linha 129, seq_adn = 'AAATGCATCGACTGATATGCGCATG'
# (como está definida, não precisamos de escrever novamente)

resultado_23_1 = seq_adn.find('A')
resultado_23_2 = seq_adn.find('T')
resultado_23_3 = seq_adn.find('CA')

print(resultado_23_1)
print(resultado_23_2)
print(resultado_23_3)

# As duas linhas abaixo estão sob comentário. Remova # para ver o erro na sua consola
# Depois coloque novamente # para conseguir correr o código novamente

# resultado_23_4 = seq_adn.index('U')
# print(resultado_23_4)

# 24-25: .startwith() e .endswith()
# vamos utilizar o valor da linha 29, website = 'www.google.com'
# (como está definida, não precisamos de escrever novamente)

resultado_24 = website.startswith('www.')
resultado_25_1 = website.endswith('.com')
resultado_25_2 = website.endswith('google')

print(resultado_24)
print(resultado_25_1)
print(resultado_25_1)

# 26: .partition()
# vamos utilizar o valor da linha 42, email = 'tiago@automation.com'
# (como está definida, não precisamos de escrever novamente)

resultado_26 = email.partition('@')

print(resultado_26)

# 27-29: .center(), .ljust() e .rjust()
# vamos utilizar o valor da linha 42, email = 'tiago@automation.com'
# (como está definida, não precisamos de escrever novamente)

resultado_27 = email.center(30, '-')
resultado_28 = email.ljust(30, '-')
resultado_29 = email.rjust(30, '-')

print(resultado_27)
print(resultado_28)
print(resultado_29)

# 30: .zfill()
pontos_1 = '20'
pontos_2 = '+20'
pontos_3 = '-20'
pontos_4 = 'a20'

resultado_30_1 = pontos_1.zfill(5)
resultado_30_2 = pontos_2.zfill(5)
resultado_30_3 = pontos_3.zfill(5)
resultado_30_4 = pontos_4.zfill(5)

print(resultado_30_1)
print(resultado_30_2)
print(resultado_30_3)
print(resultado_30_4)
