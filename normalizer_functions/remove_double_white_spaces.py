from typing import List


def remove_double_white_spaces(phrase_list: List[str]) -> List[str]:
    phrase_list_without_white_spaces = [phrase for phrase in phrase_list]
    for words in range(len(phrase_list)):
        phrase_list_without_white_spaces[words] = (phrase_list[words]).replace("  ", " ")
    return phrase_list_without_white_spaces
