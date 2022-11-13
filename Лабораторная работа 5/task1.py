from pprint import pprint
dictionary_ = [{"bin": bin(i), "dec": i, "hex": hex(i), "oct": oct(i)} for i in range(0, 16)]
pprint(dictionary_)
# TODO решить с помощью list comprehension и распечатать его
