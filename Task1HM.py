# Напишите программу, удаляющую из текста все слова, содержащие "абв"

# 'абвгдейка - это передача' = >" - это передача"

text = 'абвгдейка - это передача'

del_char = 'абв'
text = text.split()

result1 = [i for i in text if del_char not in i]

print('Original text:')
print(' '.join(text))
print('Modified text:')
print(' '.join(result1))
