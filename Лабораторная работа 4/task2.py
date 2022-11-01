def get_count_char(str_):
  one_str = "".join(main_str.split())
  low_str = one_str.lower()
  first_dict = {}
  for i in low_str:
      if i.isalpha():
          if not (i in first_dict.keys()):
              first_dict[i] = 1
          else:
              first_dict[i] += 1
  return first_dict


def calc_proc_elem(dictionary):
    calc_proc = 0
    for i in dictionary:
        calc_proc += dictionary[i]
    new_dict = {}
    for i in dictionary:
        new_dict[i] = int(dictionary[i] / calc_proc * 100)
    return new_dict

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
print(calc_proc_elem(get_count_char(main_str)))