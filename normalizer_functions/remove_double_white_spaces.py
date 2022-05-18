from typing import List


def remove_several_white_spaces(phrase_list: List[str]) -> List[str]:
    for words in range(len(phrase_list)):
        phrase_list[words] = " ".join(phrase_list[words].split())
    return phrase_list
