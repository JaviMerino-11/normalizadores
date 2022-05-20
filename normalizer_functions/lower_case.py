from typing import List


def lower_case_normalizer(phrase_list: List[str]) -> None:
    for index, word in enumerate(phrase_list):
        phrase_list[index] = word.lower()
