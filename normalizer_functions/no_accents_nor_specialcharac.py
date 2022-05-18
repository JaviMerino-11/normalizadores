from typing import List
import unidecode


def no_accents_nor_specialcharac(phrase_list: List[str]) -> List[str]:
    phrase_list_unaccented_no_special_characters = [phrase for phrase in phrase_list]
    for words in range(len(phrase_list)):
        phrase_list_unaccented_no_special_characters[words] = unidecode.unidecode(phrase_list[words])
    return phrase_list_unaccented_no_special_characters
