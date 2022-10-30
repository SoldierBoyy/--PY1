def get_count_char(str_):
    one_str = "".join(main_str.split())
    low_str = one_str.lower()
    dict_ = {}
    for char in low_str:
        if char.isalpha():
            if not (char in dict_.keys()):
                dict_[char] = 1
            else:
                dict_[char] += 1
    return dict_

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
