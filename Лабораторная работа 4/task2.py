def get_count_char(str_):
  one_str = "".join(main_str.split())
  low_str = one_str.lower()
  dic = {}
  for i in low_str:
      if i.isalpha():
          if not (i in dic.keys()):
              dic[i] = 1
          else:
              dic[i] += 1
  return dic

def part_2(dict):
    sm = 0
    for i in dict:
        sm += dict[i]
    for i in dict:
        dict[i] = int(dict[i] / sm * 100)
        return dict

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
