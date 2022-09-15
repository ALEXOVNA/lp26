# реализовано: скрипт считывает текст из файла, приводит все символы в нижний регистр,
# подсчивает частоту каждого слова в разрезе всего текста, а затем,
# создает топ-список слов, размер которого установлен в данной версии по умолчанию

import string
from collections import Counter
import config

size_top_words = 5
result_top_list = []


txt_in_lowcase = open(file=config.path_to_txt_file).read().lower()


def create_words_lower_list():
  words_lower_list = txt_in_lowcase.split()
  return words_lower_list


def find_top_words_in_txt_in_lowcase():
  item = 0

  ordered_words_list = Counter(create_words_lower_list()).most_common()
  top_words_list = ordered_words_list[0:size_top_words]
  if item < size_top_words:
    for item in range(size_top_words):
      result_top_list.append(top_words_list[item][0])
      item += 1
  print(result_top_list)


if __name__ == '__main__':
  find_top_words_in_txt_in_lowcase()

