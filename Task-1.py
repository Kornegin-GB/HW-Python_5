""" Напишите программу, удаляющую из текста все слова, содержащие "абв". """

text = 'Привет забвение котёнок абв абвеартура гав'
str = 'абв'
result = ' '.join(list(filter(lambda x: str not in x, text.split())))
print(result)
