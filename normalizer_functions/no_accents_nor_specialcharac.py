from typing import List
import unidecode


def no_accents_nor_specialcharac(phrase_list: List[str]) -> List[str]:
    for words in range(len(phrase_list)):
        phrase_list[words] = unidecode.unidecode(phrase_list[words])
    return phrase_list
