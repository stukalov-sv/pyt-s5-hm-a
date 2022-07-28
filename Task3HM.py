# Создайте два списка — один с названиями языков программирования,
# другой — с числами от 1 до длины первого.
# ['python', 'c#']
# [1,2]
# Вам нужно сделать две функции: первая из которых создаст список кортежей,
# состоящих из номера и языка, написанного большими буквами.
# [(1,'PYTHON'), (2,'C#')]
# Вторая — которая отфильтрует этот список следующим образом: если сумма очков слова
# имеет в делителях номер, с которым она в паре в кортеже, то кортеж остается,
# его номер заменяется на сумму очков.
# [сумма очков c# = 102, в делителях есть 2 с которым в паре. Значит список будет]
# [(1,'PYTHON'), (102,'C#')]
# Если нет — удаляется. Суммой очков называется сложение порядковых номеров букв в слове.

# Cложите получившиеся числа и верните из функции в качестве ответа
# вместе с преобразованным списком


def get_tuple_lst(items_lst: list, keys_lst: list) -> list:
    temp_items_lst = [i.upper() for i in items_lst]
    result_lst = list(zip(keys_lst, temp_items_lst))
    return result_lst


def get_filtered_tuple_items_sum(tple_lst: list):
    temp_item_lst = []
    temp_number_lst = []
    result_number = 0

    for item in tple_lst:
        temp_lst = list(item)
        temp_result = 0
        for k in temp_lst[1].encode('utf-8'):
            temp_result += k
        if temp_result % temp_lst[0] == 0:
            temp_item_lst.append(temp_lst[1])
            temp_number_lst.append(temp_result)
            result_number += temp_result

    result_tple_lst = list(zip(temp_number_lst, temp_item_lst))

    return(result_tple_lst, result_number)


language_lst = ['python', 'c#', 'c', 'c++', 'java', 'javascript', 'sql']
language_numbers = [i + 1 for i, item in enumerate(language_lst)]

tple_lst = get_tuple_lst(language_lst, language_numbers)

print(f'Original tuple list:\n{tple_lst}')

result_lst, result_sum = get_filtered_tuple_items_sum(tple_lst)

print(f'Modified tuple list:\n{result_lst}')
print(f'Control amount: {result_sum}')
