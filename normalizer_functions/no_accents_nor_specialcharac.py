from typing import List
import unidecode


def no_accents_nor_specialcharac(phrase_list: List[str]) -> None:
    for index, word in enumerate(phrase_list):
        phrase_list[index] = unidecode.unidecode(word)
