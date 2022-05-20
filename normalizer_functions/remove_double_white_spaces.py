from typing import List


def remove_several_white_spaces(phrase_list: List[str]) -> None:
    for index, word in enumerate(phrase_list):
        phrase_list[index] = " ".join(word.split())
